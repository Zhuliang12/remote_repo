# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/4/9 3:49

import matplotlib.pyplot as plt
import math
import torch
from torchvision.models import resnet50
from math import cos, pi


def adjust_learning_rate(optimizer, current_epoch, max_epoch, lr_min=0, lr_max=0.1, warmup=True):
    warmup_epoch = 3 if warmup else 0
    if current_epoch < warmup_epoch:
        lr = lr_max * current_epoch / warmup_epoch
    elif current_epoch < max_epoch:
        lr = lr_min + (lr_max - lr_min) * (
                1 + cos(pi * (current_epoch - warmup_epoch) / (max_epoch - warmup_epoch))) / 2
    else:
        lr = lr_min + (lr_max - lr_min) * (
                1 + cos(pi * (current_epoch - max_epoch) / (max_epoch))) / 2
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr


model = resnet50(pretrained=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

lr_max = 0.01
lr_min = 0.001
max_epoch =  200
lrs = []
for epoch in range(10 * 20):
    adjust_learning_rate(optimizer=optimizer, current_epoch=epoch, max_epoch=max_epoch, lr_min=lr_min, lr_max=lr_max,
                         warmup=True)
    print(optimizer.param_groups[0]['lr'])
    lrs.append(optimizer.param_groups[0]['lr'])
    optimizer.step()

plt.plot(lrs)

plt.show()
