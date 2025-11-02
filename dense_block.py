# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/15 18:02

'''
稠密连接块
'''

import torch
import torch.nn as nn
import torch.nn.functional as F

from d2l import torch as d2l


def conv_block(input_channels, out_channels):
    return nn.Sequential(
        nn.BatchNorm2d(input_channels),
        nn.ReLU(),
        nn.Conv2d(input_channels, out_channels, kernel_size=3, padding=1)
    )


# 一个稠密块由多个卷积块组成，每个卷积块使用相同数量的输出通道，
# 然而，在前向传播中，我们将每个卷积块的输入和输出在通道维上连接

class DenseBlock(nn.Module):
    def __init__(self, num_convs, input_channels, num_channels):
        super(DenseBlock, self).__init__()
        layer = []
        for i in range(num_convs):
            layer.append(conv_block(
                input_channels + num_channels * i, num_channels)
            )
        self.net = nn.Sequential(*layer)

    def forward(self, x):
        for blk in self.net:
            y = blk(x)
            # 将通道数添加到一起
            x = torch.cat((x, y), dim=1)

        return x


# 一个有2个输出通道数为10的DenseBlock。 使用通道数为3的输入时，我们会得到通道数为3+2×10=23的输出。
# 卷积块的通道数控制了输出通道数相对于输入通道数的增长，因此也被称为增长率（growth rate）
blk = DenseBlock(6, 4, 10)
print(blk)
X = torch.randn(4, 4, 8, 8)
Y = blk(X)
# print(Y)
print(Y.shape)


# torch.Size([4, 23, 8, 8])

# 过渡层
def transition_block(input_channels, num_channels):
    return nn.Sequential(
        nn.BatchNorm2d(input_channels),
        nn.ReLU(),
        nn.Conv2d(input_channels, num_channels, kernel_size=1),
        nn.AvgPool2d(kernel_size=2, stride=2)
    )


a = transition_block(64, 32)
Y = a(Y)
# print(Y)
print(Y.shape)
# torch.Size([4, 12, 4, 4])

# num_channels为当前的通道数
num_channels, grow_rate = 64, 32
num_convs_in_dense_blocks = [4, 4, 4, 4]
blks = []
for i, num_convs in enumerate(num_convs_in_dense_blocks):
    blks.append(DenseBlock(num_convs, num_channels, grow_rate))
    # 上一个稠密块的输出通道
    num_channels += num_convs * grow_rate
    # 在稠密快之间添加一个转换层，使得通道数量减半
    if i != len(num_convs_in_dense_blocks) - 1:
        blks.append(transition_block(num_channels, num_channels // 2))
        num_channels = num_channels // 2

net = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=4, kernel_size=1, padding=1),
    blk,
    *blks,
    nn.BatchNorm2d(num_channels), nn.ReLU(),
    nn.AdaptiveAvgPool2d((1, 1)),
    nn.Flatten(),
    nn.Linear(num_channels, 10))

lr, num_epochs, batch_size = 0.1, 10, 16
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size, resize=96)
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())  # 显存太小 ，运行不了
