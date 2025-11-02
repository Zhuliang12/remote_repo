# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/14 21:39

import torch
import torch.nn as nn


class SE_block(nn.Module):
    def __init__(self, channels, ratio=16):
        super(SE_block, self).__init__()
        # 对空间信息进行压缩
        self.avgpool = nn.AdaptiveAvgPool2d(1)

        # 经过两次全连接层，学习不同通道的重要性
        self.fc=nn.Sequential(
            nn.Linear(channels,channels//16,False),
            nn.ReLU(),
            nn.Linear(channels//16,channels,False),
            nn.Sigmoid()
        )

    def forward(self,x):
        b,c,_,_=x.size() # 取出
