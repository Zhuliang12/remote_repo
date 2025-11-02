#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/10/20 15:22

import concurrent.futures
import os
import random
import shutil
import pathlib


def pathlib_mkdir(path):
    if not pathlib.Path.exists(path):
        pathlib.Path.mkdir(path)


def split(dara_dir, proportion, save_dir):
    assert pathlib.Path.exists(dara_dir), print('{} does not exist, please input again'.format(data_dir))


def mkdir(check_dir):
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)


def split_dataset(data_dir, proportion, save_dir):
    assert os.path.exists(data_dir), \
        print('{} does not exist, please input again!'.format(data_dir))

    # 检查保存路径是否存在，若不存在则创建
    mkdir(save_dir)
    mkdir(os.path.join(save_dir, "train"))
    mkdir(os.path.join(save_dir, "valid"))
    if len(proportion) == 2:
        mkdir(os.path.join(save_dir, "test"))

    # 获取数据集中所有的图片路径
    img_list = os.listdir(data_dir)
    # print(img_list)
    '''
    这边要修改想要划分数据集的后缀名
    '''
    img_list = [os.path.join(data_dir, img) for img in img_list if img.endswith('.jpg') or img.endswith('.png')]

    # 随机打乱数据集顺序
    random.shuffle(img_list)

    # 计算划分后的数据集大小
    if len(proportion) == 1:
        train_size = int(len(img_list) * proportion[0])
    elif len(proportion) == 2:
        train_size = int(len(img_list) * proportion[0])
        val_size = int(len(img_list) * proportion[1])

    # 将数据集划分为训练集、验证集和测试集（若有）
    if len(proportion) == 1:
        train_list = img_list[:train_size]
        val_list = img_list[train_size:]
        for img in train_list:
            shutil.move(img, os.path.join(save_dir, "train"))
        for img in val_list:
            shutil.move(img, os.path.join(save_dir, "valid"))
    elif len(proportion) == 2:
        train_list = img_list[:train_size]
        val_list = img_list[train_size:train_size + val_size]
        test_list = img_list[train_size + val_size:]
        for img in train_list:
            shutil.move(img, os.path.join(save_dir, "train"))
        for img in val_list:
            shutil.move(img, os.path.join(save_dir, "valid"))
        for img in test_list:
            shutil.move(img, os.path.join(save_dir, "test"))


if __name__ == "__main__":
    data_dir = r'F:\LT_DATASETS\PUBLIC\DATASET_ANIMAL_AND_BIRD\DETECTION\train\images/'  # 数据集目录
    proportion = [0.95, 0.05]  # 划分比例
    save_dir = r'F:\LT_DATASETS\PUBLIC\DATASET_ANIMAL_AND_BIRD\DETECTION\train/'  # 保存路径
    split_dataset(data_dir, proportion, save_dir)
    print('finished!')
