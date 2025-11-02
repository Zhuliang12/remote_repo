# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/9 16:26

'''
上采样 torch.nn.Upsample(size=None,size_factor=None,mode='nearest',align_corners=None)
size: 输出空间大小
size_factor : 空间大小乘积
mode: 上采样的方式 有 nearest邻近插值,linear线性插值,bilinear双线性插值,bicubic,trilinear三线性插值, default=nearest
align_corners:
Upsample 既能上采样也可以下采样
torch 中下采样 推荐使用 interpolate
'''

import torch.nn.functional as F
import torch
import torch.nn as nn

# nearest 最近邻插值法
input = torch.arange(1, 5, dtype=torch.float32).view(1, 1, 2, 2)
print(input)
sample = nn.Upsample(scale_factor=2, mode='nearest')  # 进行上采样
print(sample(input))
'''
tensor([[[[1., 2.],
          [3., 4.]]]])
tensor([[[[1., 1., 2., 2.],
          [1., 1., 2., 2.],
          [3., 3., 4., 4.],
          [3., 3., 4., 4.]]]])'''

# 双线性插值

sample1 = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False)
sample2 = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
print(sample1(input))
print(sample2(input))
'''
tensor([[[[1.0000, 1.2500, 1.7500, 2.0000],
          [1.5000, 1.7500, 2.2500, 2.5000],
          [2.5000, 2.7500, 3.2500, 3.5000],
          [3.0000, 3.2500, 3.7500, 4.0000]]]])
tensor([[[[1.0000, 1.3333, 1.6667, 2.0000],
          [1.6667, 2.0000, 2.3333, 2.6667],
          [2.3333, 2.6667, 3.0000, 3.3333],
          [3.0000, 3.3333, 3.6667, 4.0000]]]])'''

input1 = torch.arange(1, 13, dtype=torch.float32).view(1, 3, 2, 2)
# sample = nn.Upsample(size=(5), mode='nearest')  # 使用这行，错误消失
sample3 = nn.Upsample(scale_factor=2.5, mode='nearest')  # 报错：如下
print(input)
print(sample3(input1))
'''
tensor([[[[ 1.,  2.],
          [ 3.,  4.]],

         [[ 5.,  6.],
          [ 7.,  8.]],

         [[ 9., 10.],
          [11., 12.]]]])
/home/wangyh/anaconda3/envs/torch/lib/python3.6/site-packages/torch/nn/functional.py:3103: UserWarning: The default behavior for interpolate/upsample with float scale_factor changed in 1.6.0 to align with other frameworks/libraries, and now uses scale_factor directly, instead of relying on the computed output size. If you wish to restore the old behavior, please set recompute_scale_factor=True. See the documentation of nn.Upsample for details. 
  warnings.warn("The default behavior for interpolate/upsample with float scale_factor changed "
tensor([[[[ 1.,  1.,  1.,  2.,  2.],
          [ 1.,  1.,  1.,  2.,  2.],
          [ 1.,  1.,  1.,  2.,  2.],
          [ 3.,  3.,  3.,  4.,  4.],
          [ 3.,  3.,  3.,  4.,  4.]],

         [[ 5.,  5.,  5.,  6.,  6.],
          [ 5.,  5.,  5.,  6.,  6.],
          [ 5.,  5.,  5.,  6.,  6.],
          [ 7.,  7.,  7.,  8.,  8.],
          [ 7.,  7.,  7.,  8.,  8.]],

         [[ 9.,  9.,  9., 10., 10.],
          [ 9.,  9.,  9., 10., 10.],
          [ 9.,  9.,  9., 10., 10.],
          [11., 11., 11., 12., 12.],
          [11., 11., 11., 12., 12.]]]])
'''

