# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/4/2 13:48

import torch
from torchvision.ops import deform_conv2d

h = w = 3

# batch_size, num_channels, out_height, out_width
x = torch.arange(h * w * 3, dtype=torch.float32).reshape(1, 3, h, w)
print(x)

# to show the effect of offset more intuitively, only the case of kh=kw=1 is considered here
offset = torch.FloatTensor(
    [  # create our predefined offset with offset_groups = 3
        0, -1,  # sample the left pixel of the centroid pixel
        0, 1,  # sample the right pixel of the centroid pixel
        -1, 0,  # sample the top pixel of the centroid pixel
    ]  # here, we divide the input channels into offset_groups groups with different offsets.
).reshape(1, 2 * 3 * 1 * 1, 1, 1)
# here we use the same offset for each local neighborhood in the single channel
# so we repeat the offset to the whole space: batch_size, 2 * offset_groups * kh * kw, out_height, out_width
offset = offset.repeat(1, 1, h, w)

weight = torch.FloatTensor(
    [
        [1, 0, 0],  # only extract the first channel of the input tensor
        [0, 1, 0],  # only extract the second channel of the input tensor
        [1, 1, 0],  # add the first and the second channels of the input tensor
        [0, 0, 1],  # only extract the third channel of the input tensor
        [0, 1, 0],  # only extract the second channel of the input tensor
    ]
).reshape(5, 3, 1, 1)
deconv_shift = deform_conv2d(x, offset=offset, weight=weight)
print(deconv_shift)

"""
tensor([[
[[ 0.,  0.,  1.],  # offset=(0, -1) the first channel of the input tensor
[ 0.,  3.,  4.],  # output hw indices (1, 2) => (1, 2-1) => input indices (1, 1)
[ 0.,  6.,  7.]], # output hw indices (2, 1) => (2, 1-1) => input indices (2, 0)

[[10., 11.,  0.],  # offset=(0, 1) the second channel of the input tensor
[13., 14.,  0.],  # output hw indices (1, 1) => (1, 1+1) => input indices (1, 2)
[16., 17.,  0.]], # output hw indices (2, 0) => (2, 0+1) => input indices (2, 1)

[[10., 11.,  1.],  # offset=[(0, -1), (0, 1)], accumulate the first and second channels after being sampled with an offset.
[13., 17.,  4.],
[16., 23.,  7.]],

[[ 0.,  0.,  0.],  # offset=(-1, 0) the third channel of the input tensor
[18., 19., 20.],  # output hw indices (1, 1) => (1-1, 1) => input indices (0, 1)
[21., 22., 23.]], # output hw indices (2, 2) => (2-1, 2) => input indices (1, 2)

[[10., 11.,  0.],  # offset=(0, 1) the second channel of the input tensor
[13., 14.,  0.],  # output hw indices (1, 1) => (1, 1+1) => input indices (1, 2)
[16., 17.,  0.]]  # output hw indices (2, 0) => (2, 0+1) => input indices (2, 1)
]])
"""
