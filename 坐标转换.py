# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/15 17:12

import numpy as np

import os

# train_1 = np.loadtxt('D:/mydata/stervel/train/images_labels_all_rec/txt_labels_all/train_1.txt')
with open('D:/mydata/stervel/train/images_labels_all_rec/txt_labels_all/train_1.txt') as txt:
    if not os.path.getsize('D:/mydata/stervel/train/images_labels_all_rec/txt_labels_all/train_1.txt'):
        print('D:/mydata/stervel/train/images_labels_all_rec/txt_labels_all/train_1.txt', " is empty!")


# print(train_1)  # 得到的浮点数
# print(len(np.array(train_1).shape))
# for line in train_1:
# print(int(float(line[0])))

def xyxy2xywh(x):
    # 将坐标转换成 xywh 左上和右下
    # Convert nx4 boxes from [x1, y1, x2, y2] to [x, y, w, h] where xy1=top-left, xy2=bottom-right
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = (x[:, 0] + x[:, 2]) / 2  # x center
    y[:, 1] = (x[:, 1] + x[:, 3]) / 2  # y center
    y[:, 2] = x[:, 2] - x[:, 0]  # width
    y[:, 3] = x[:, 3] - x[:, 1]  # height
    return y


def xywh2xyxy(x):
    # 将宽高转换为 坐标 左上和右下
    # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y


import torch

x2 = torch.rand(6, 6)
print(x2)

for i, d in enumerate(x2):
    if d is not None and len(d):
        d = d.clone()

        b = xyxy2xywh(d[:, :4])
        b[:, 2:] = b[:, 2:].max(1)[0].unsqueeze(1)  # 矩形到正方形
        b[:, 2:] = b[:, 2:] * 1.3 + 30  # pad
        d[:, :4] = xywh2xyxy(b).long()

        print(d)
'''
IndexError: too many indices for tensor of dimension 1'''