# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/4/2 22:46

import cv2
import numpy as np
import random


def mosaic_augmentation(images, labels, size=416, p=0.5):
    """
    Mosaic数据增强
    :param images: 图像列表
    :param labels: 标签列表
    :param size: 输出图像大小
    :param p: 概率
    :return: 增强后的图像和标签
    """
    assert len(images) == len(labels), "图像和标签数量不一致！"
    assert len(images) >= 4, "图像数量必须大于等于4！"

    if random.random() > p:
        return images, labels

    # 随机选择4张图像
    indices = random.sample(range(len(images)), 4)
    img1, img2, img3, img4 = images[indices]
    label1, label2, label3, label4 = labels[indices]

    # 随机选择拼接位置
    x = random.randint(size // 2, size - 1)
    y = random.randint(size // 2, size - 1)

    # 拼接图像
    mosaic = np.zeros((size, size, 3), dtype=np.uint8)
    mosaic[:y, :x] = cv2.resize(img1, (x, y))
    mosaic[:y, x:] = cv2.resize(img2, (size - x, y))
    mosaic[y:, :x] = cv2.resize(img3, (x, size - y))
    mosaic[y:, x:] = cv2.resize(img4, (size - x, size - y))

    # 随机裁剪
    cx = random.randint(size // 2, size - 1)
    cy = random.randint(size // 2, size - 1)
    dx = size - cx
    dy = size - cy
    mosaic = mosaic[cy - size // 2:cy + dy - size // 2, cx - size // 2:cx + dx - size // 2]

    # 随机水平翻转
    if random.random() > 0.5:
        mosaic = cv2.flip(mosaic, 1)
        label1[:, 1] = 1 - label1[:, 1]
        label2[:, 1] = 1 - label2[:, 1]
        label3[:, 1] = 1 - label3[:, 1]
        label4[:, 1] = 1 - label4[:, 1]

    # 随机垂直翻转
    if random.random() > 0.5:
        mosaic = cv2.flip(mosaic, 0)
        label1[:, 2] = 1 - label1[:, 2]
        label2[:, 2] = 1 - label2[:, 2]
        label3[:, 2] = 1 - label3[:, 2]
        label4[:, 2] = 1 - label4[:, 2]

    # 颜色平衡
    mosaic = cv2.cvtColor(mosaic, cv2.COLOR_BGR2HSV)
    mosaic[:, :, 1] = mosaic[:, :, 1] * (0.8 + random.random() * 0.4)
    mosaic[:, :, 2] = mosaic[:, :, 2] * (0.8 + random.random() * 0.4)
    mosaic = cv2.cvtColor(mosaic, cv2.COLOR_HSV2BGR)

    # 更新标签
    label = np.vstack((label1, label2, label3, label4))
    label[:, 3:] = label[:, 3:] * size
    label[:, 1] = label[:, 1] * cx + label[:, 3] / 2 - size // 2
    label[:, 2] = label[:, 2] * cy + label[:, 4] / 2 - size // 2

    return mosaic, label
