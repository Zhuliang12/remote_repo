# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/13 20:40
import argparse
import logging
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from pathlib import Path
from torch import optim
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm

import wandb
from evaluate import evaluate
from unet import UNet
from utils.data_loading import BasicDataset, CarvanaDataset
from utils.dice_score import dice_loss

dir_img = Path('./data/imgs/')
dir_mask = Path('./data/masks/')
dir_checkpoint = Path('./checkpoints/')


def train_model(
        model,
        device,
        epochs: int = 5,
        batch_size: int = 1,
        learning_rate: float = 1e-5,
        val_percent: float = 0.1,
        save_checkpoint: bool = True,
        img_scale: float = 0.5,
        amp: bool = False,
        weight_decay: float = 1e-8,
        momentum: float = 0.999,
        gradient_clipping: float = 1.0,
):
    # 创建数据集
    try:
        dataset = CarvanaDataset(dir_img, dir_mask, img_scale)
    except(AssertionError, RuntimeError):
        dataset = BasicDataset(dir_img, dir_mask, img_scale)

    # 划分 训练/验证集
    n_val = int(len(dataset) * val_percent)
    n_train = len(dataset) - n_val
    train_set, val_set = random_split(dataset, [n_train, n_val], generator=torch.Generator().manual_seed(0))

    # 创建数据加载器
    loader_args = dict(batch_size=batch_size, num_workers=os.cpu_count(), pin_memory=True)
    # 训练加载器
    train_loader = DataLoader(train_set, shuffle=True, **loader_args)
    # 验证集训练加载器
    val_loader = DataLoader(val_set, shuffle=False, drop_last=True, **loader_args)

    # 初始化日志记录
    experiment = wandb.init(project='U-Net', resume='allow', anonymous='must')
    experiment.config.update(
        dict(epochs=epochs, batch_size=batch_size, learning_rate=learning_rate,
             val_percent=val_percent, save_checkpoint=save_checkpoint, img_scale=img_scale, amp=amp)
    )

    logging.info(f'''Starting training:
        Epochs:         {epochs}
        Batch size:     {batch_size}
        Learning rate:  {learning_rate}
        Training size:  {n_train}
        Validation size:{n_val}
        Checkpoints:    {save_checkpoint}
        Device:         {device.type}
        Images scaling: {img_scale}
        Mixed Precision:{amp}
    ''')

    # 为AMP设置优化器、损失、学习率调度器和损失缩放
    optimizer = optim.RMSprop(model.parameters(),
                              lr=learning_rate, weight_decay=weight_decay, momentum=momentum, foreach=True)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'max', patience=5)
    grad_scaler = torch.cuda.amp.GradScaler(enabled=amp)
    criterion = nn.CrossEntropyLoss() if model.n_classes > 1 else nn.BCEWithLogitsLoss()
    global_step = 0

    # 开始训练
    for epoch in range(1, epochs + 1):
        model.trian()
        epoch_loss = 0
        with tqdm(total=n_train, desc=f'Epoch{epoch}/{epochs}', unit='img') as pbar:
            for batch in train_loader:
                images, true_masks = batch['image'], batch['mask']

                assert images.shape[1] == model.n_classes, \
                    f'network has been defined with {model.n_classes} input channels,' \
                    f'but loaded images have {images.shape[1]} channels.please check that' \
                    'the images are loaded correctly'

                images = images.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
                true_masks = true_masks.to(device=device, dtype=torch.long)

                with torch.autocast(device.type if device.type != 'mps' else 'cpu', enabled=amp):
                    masks_pred = model(images)
                    if model.n_classes == 1:
                        loss = criterion(masks_pred.squeeze(1), true_masks.float())
                        loss += dice_loss(F.sigmoid(masks_pred.squeeze(1)), true_masks.float(), multiclass=False)
                    else:
                        loss = criterion(masks_pred, true_masks)
                        loss += dice_loss(
                            F.softmax(masks_pred, dim=1).float(),
                            F.one_hot(true_masks, model.n_classes).permute(0, 3, 1, 2).float(),
                            multiclass=True
                        )

                optimizer.zero_grad(set_to_none=True)
                grad_scaler.scale(loss).backward()  # 反向传播
                torch.nn.utils.clip_grad_norm_(model.parameters(), gradient_clipping)
                grad_scaler.step(optimizer)
                grad_scaler.update()

                pbar.update(images.shape[0])
                global_step += 1
                epoch_loss += loss.item()
                experiment.log({
                    'train loss': loss.item(),
                    'step': global_step,
                    'epoch': epoch
                })
                pbar.set_postfix(**{'loss(batch)': loss.item()})

                # evalution round
                divison_step = (n_train // (5 * batch_size))
                if divison_step > 0:
                    if global_step % divison_step == 0:
                        histograms = {}
                        for tag, value in model.named_parameters():
                            tag = tag.replace('/', '.')
                            if not torch.isinf(value).any():
                                histograms['Weights/' + tag] = wandb.Histogram(value.data.cpu())
                            if not torch.isinf(value.grad).any():
                                histograms['Gradients/' + tag] = wandb.Histogram(value.grad.data.cpu())

                        val_score = evaluate(model, val_loader, device, amp)
                        scheduler.step(val_score)

                        logging.info('Validation Dice score:{}'.format(val_score))
                        try:
                            experiment.log({
                                'learning rate': optimizer.param_groups[0]['lr'],
                                'validation Dice': val_score,
                                'images': wandb.Image(images[0].cpu()),
                                'masks': {
                                    'true': wandb.Image(true_masks[0].float().cpu()),
                                    'pred': wandb.Image(masks_pred.argmax(dim=1)[0].float().cpu()),
                                },
                                'step': global_step,
                                'epoch': epoch,
                                **histograms
                            })
                        except:
                            pass

        if save_checkpoint:
            Path(dir_checkpoint).mkdir(parents=True,exist_ok=True)
            state_dict=model.state_dict()
            state_dict['mask_value']=dataset.mask_values
            torch.save(state_dict,str(dir_checkpoint/'checkpoint_epoch{}.path'.format(epoch)))
            logging.info(f'Checkpoint{epoch}saved!')


def get_args():
    parser=argparse.ArgumentParser(description='Train the UNet on images and target masks')
    parser.add_argument('--epochs','-e',metavar='E',type=int,default=5,help='Number of epochs')
    parser.add_argument('--batch-size','-b',dest='batch_size',metavar='B',type=int,default=1,help='Batch size')
    parser.add_argument('--learning-rate','-l',metavar='LR',type=float,default=1e-5,help='Learning rate',dest='lr')
    parser.add_argument('--load','-f',type=str,default=False,help='Load model from a .pth file')
    parser.add_argument('--scale','-s',type=float,default=0.5,help='Downscaling factor of the images')
    parser.add_argument('--validation','-v',dest='val',type=float,default=10.0,
                        help='Percent of the data that is used as validation (0-100)')
    parser.add_argument('--amp',action='store_true',default=False,help='Use mixed precision')
    parser.add_argument('--bilinear',action='store_true',default=False,help='Use bilinear upsampling')
    parser.add_argument('--classes','-c',type=int,default=2,help='Number of classes')

    return parser.parse_args()

if __name__=='__main__':
    args=get_args()

    logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(message)s')
    device=torch.device('cuda'if torch.cuda.is_available() else 'cpu')
    logging.info(f'Using device{device}')

    model =UNet(n_channels=3,n_classes=args.classes,bilinear=args.bilinear)
    model=model.to(memory_format=torch.channels_last)

    logging.info(f'Network:\n'
                 f'\t{model.n_channels}input channels\n'
                 f'\t{model.n_classes} output channels(classes)\n'
                 f'\t{"Bilinear"if model.bilinear else "Transposed conv"}upscalling')

    if args.load:
        state_dict=torch.load(args.load,map_location=device)
        del state_dict['mask_value']
        model.load_state_dict(state_dict)
        logging.info(f'Model loaded from {args.load}')

    model.to(device=device)
    try:
        train_model(
            model=model,
            epochs=args.epochs,
            batch_size=args.batch_size,
            learning_rate=args.lr,
            device=device,
            img_scale=args.scale,
            val_percent=args.val/100,
            amp=args.amp
        )
    except torch.cuda.OutOfMemoryError:
        logging.error('Detected OutOfMemoryError! '
                      'Enabling checkpointing to reduce memory usage, but this slows down training. '
                      'Consider enabling AMP (--amp) for fast and memory efficient training')
        torch.cuda.empty_cache()
        model.use_checkpointing()
        train_model(
            model=model,
            epochs=args.epochs,
            batch_size=args.batch_size,
            learning_rate=args.lr,
            device=device,
            img_scale=args.scale,
            val_percent=args.val / 100,
            amp=args.amp
        )

