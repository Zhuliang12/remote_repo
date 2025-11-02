# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/9 19:25

import torch
import torch.nn as nn
import torch.nn.functional as F

original_values = torch.randn([2, 2, 4, 4])
original_values1 = torch.randn([2, 1, 2, 2])
print('original values:', original_values, '\n')
print(original_values1, original_values1.shape)
print('original values的shape:', original_values.shape)

# 进行填充

x1 = F.pad(original_values, [0, 0, 2, 2])
# [左，右，上，下]的填充
print(x1)


class DoubleConv(nn.Module):
    # 2*(conv->bn->relu)
    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        if not mid_channels:
            mid_channels = out_channels
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)


class Up(nn.Module):
    ''' Upsampling the double conv'''

    def __init__(self, in_channels, out_channels, bilinder=True):
        super().__init__()
        if bilinder:
            self.up = nn.Upsample(scale_factor=2, mode='bilinder', align_corners=True)
            self.conv = DoubleConv(in_channels, out_channels, in_channels // 2)  # 这里是两个卷积层
        else:
            self.up = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2)
            self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):

        x1 = self.up(x1)
        # input is CHW
        diffX = x2.size()[2] - x1.size()[2]
        diffY = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2])
        # 对于x1进行上下左右填充
        x = torch.cat([x1, x2], dim=1)  # dim=0为列方向，1为横方向
        return self.conv(x)
        # 这里也是两个卷积层


diffX = original_values.size()[2] - original_values1.size()[2]
diffY = original_values.size()[3] - original_values1.size()[3]

x1 = F.pad(original_values1, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2])

print(x1, x1.shape)  # torch.Size([2, 1, 4, 4])
x = torch.cat([x1, original_values], dim=1)
print(x, x.shape)  # torch.Size([2, 3, 4, 4])
# x=DoubleConv(3,64)
# x=nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3,stride=1,padding=1,bias=True)
# print(x)
# 无法读取卷积层内的参数
