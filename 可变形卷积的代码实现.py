# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/4/2 17:03

import torch
import torch.nn.functional as F


class DeformableConv2d(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=1):
        super(DeformableConv2d, self).__init__()
        self.offset_conv = torch.nn.Conv2d(in_channels, kernel_size * kernel_size * 2, kernel_size=kernel_size,
                                           stride=stride, padding=padding)
        self.offset_conv.weight.data.zero_()
        self.offset_conv.bias.data.zero_()
        self.conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding)
        self.conv.weight.data.normal_(0, 0.01)
        self.conv.bias.data.zero_()
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

    def forward(self, x):
        offset = self.offset_conv(x)
        offset = offset.view(offset.size(0), 2 * self.kernel_size * self.kernel_size, offset.size(2), offset.size(3))
        offset = F.sigmoid(offset)
        x = F.conv2d(x, self.conv.weight, self.conv.bias, self.stride, self.padding)
        x = F.conv2d(x, offset, stride=self.stride, padding=self.padding, groups=x.size(1))
        return x
