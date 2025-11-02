# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/4/7 1:12
import torch
import torch.nn as nn


class ImplicitM(nn.Module):  # 1初始化
    def __init__(self, channel, mean=0., std=.02):  # 方差代表离散程度  标准差代表一组数据离平均值的离散程度
        super(ImplicitM, self).__init__()
        self.channel = channel
        self.mean = mean
        self.std = std
        self.implicit = nn.Parameter(torch.ones(1, channel, 1, 1))
        nn.init.normal_(self.implicit, mean=self.mean, std=self.std)

    def forward(self, x):
        return self.implicit * x


class ImplicitA(nn.Module):
    def __init__(self, channel, mean=0., std=.02):  # 0 初始化
        super(ImplicitA, self).__init__()
        self.channel = channel
        self.mean = mean
        self.std = std
        self.implicit = nn.Parameter(torch.zeros(1, channel, 1, 1))  # 将这些参数变成可以训练的参数
        nn.init.normal_(self.implicit, mean=self.mean, std=self.std)

    def forward(self, x):
        return self.implicit + x


anchors = [[12, 16, 19, 36, 40, 28], [36, 75, 76, 55, 72, 146], [142, 110, 192, 243, 459, 401]]
ch = [256, 512, 1024]
nc = 4
na = len(anchors[0]) // 2

x = torch.rand((3, 1, 4, 4))


ia_cls = nn.ModuleList(ImplicitA(x) for x in ch)
im_cls = nn.ModuleList(ImplicitM(nc * na) for _ in ch)
m_cls = nn.ModuleList(
            nn.Sequential(nn.Conv2d(x, x, 3), nn.Conv2d(x, na * nc, 1)) for x in ch)
mste = nn.ModuleList(nn.Conv2d(x, 27, 1) for x in ch)

bs, _, ny, nx = x.shape

x=nn.Parameter(torch.zeros(1,12,1,1))
x=nn.init.normal_(x,0.,0.02)
print(x)
print(m_cls,'\n',im_cls,'\n',ia_cls)
print(ImplicitA)
print(mste)

