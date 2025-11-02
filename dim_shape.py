# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/12 20:39

import torch
import numpy as np

a = torch.randn([2, 3, 4])
print(a.shape[-1])  # 获得最后一个维度
print(a.ndim)  # 获取其维度

b = a.reshape(-1, a.shape[-1])
print(b.shape)  # [6,4]

print(np.unique(b, axis=0))  # 按行遍历

img = torch.randn([64, 64, 3])  # [64,64,3]
# print(img)
print(img.size())
# np.unsqueeze(a,axis=0)
img = img.unsqueeze(0)  # 扩充维度
# Size([1, 64, 64, 3])
img = img.squeeze(0)  # 删除维度
print(img.size())

import torch
import torch.nn as nn
import torch.nn.functional as F
import math

in_channels = 1  # 输入的通道数
out_channels = 1  # 输出的通道数
kernel_size = 7  # 卷积核大小
batch_size = 1  # 样本的数目
bias = False
input_size = [batch_size, in_channels, 64, 64]

conv_layer1 = torch.nn.Conv2d(in_channels, out_channels, kernel_size, bias=bias, padding=3, stride=2)  # 实例化二维卷积的对象
# bn_layer = torch.nn.BatchNorm2d(out_channels, eps=1e-5)
# act_layer = torch.nn.ReLU(inplace=True)
# conv_layer2 = torch.nn.Conv2d(3, out_channels, kernel_size, bias=bias, padding=1)
input_feature_map = torch.randn(input_size)  # 生成输入，调用正态分布的随机函数
print(input_feature_map, '\n', input_feature_map.size())
output_feature_map1 = conv_layer1(input_feature_map)  # 将input_feature_map作为conv_layer的输入  经过一层卷积
print('output_feature_map1=', output_feature_map1, '\n', output_feature_map1.size())
# bn_output = bn_layer(output_feature_map1)
# act = act_layer(bn_output)
# output_feature_map2 = conv_layer2(act)  # 经过两层卷积
# print('output_feature_map1=', bn_output)
# print('激活：', act)
# print('output_feature_map2=', output_feature_map2)

# output_feature_map1 = F.conv2d(input_feature_map, conv_layer1.weight, padding=1)

# print(output_feature_map)
# print(output_feature_map1)
# print(torch.allclose(output_feature_map1, output_feature_map1))
# 在一定的误差允许内，判断两个值是否相等

# out1 = F.softmax(output_feature_map2, dim=1)  # 使用softmax 需要声明dim ，dim=0按列计算，dim=1表示按行计算
# print(out1)
# out3 = torch.sigmoid(output_feature_map2)
# print('out3=', out3)
# out2 = torch.sigmoid(output_feature_map2)[0]
# print('out2=', out2)
