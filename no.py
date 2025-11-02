# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/30 23:16
import math

import torch
import torch.nn as nn
import numpy as np

out_channels = 4
in_channels = 4
kernel_size = (3, 3)
empty = torch.empty(out_channels, in_channels, *kernel_size)
print('empty=', empty)
print('empty_size=', empty.size())
weight = nn.Parameter(empty)
print(weight, weight.size())
x=torch.rand()
out_channels_offset_mask = (1 * 3 *kernel_size[0] * kernel_size[1])
bias=nn.Parameter(torch.empty(out_channels))
# print(out_channels_offset_mask)
out_offset_mask=nn.Conv2d(4,out_channels_offset_mask,kernel_size,stride=1,padding=1,bias=True)
out_offset_mask=out_offset_mask(x)
print(out_offset_mask.size())

for k in kernel_size:
    out_channels *= k
std = 1. / math.sqrt(out_channels)
print(std)
new = weight.data.uniform_(-std, std)
print(new)
