#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/11/1 12:22

import torch
import torch.nn.functional as F

import torch
import torch.nn.functional as F


def simclr_nt_xent_loss(x1, x2, temperature=0.13):
    # 计算x1, x2的单位向量
    norm_x1 = F.normalize(x1, dim=1)
    norm_x2 = F.normalize(x2, dim=1)

    # 计算余弦相似度矩阵
    similarity_matrix = torch.mm(norm_x1, norm_x2.t())

    # 构造同类样本对和异类样本对的标签
    labels = torch.arange(similarity_matrix.size(0)).to(x1.device)

    # 同类样本对交叉熵损失
    positive_loss = F.cross_entropy(similarity_matrix / temperature, labels)

    # 异类样本对交叉熵损失
    negative_loss = F.cross_entropy(similarity_matrix.T / temperature, labels)

    # 计算总损失
    loss = positive_loss + negative_loss

    return loss


# 示例使用
x1 = torch.tensor([[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
                   [10., 11., 12., 13., 14., 15., 16., 17., 18., 19.],
                   [20., 21., 22., 23., 24., 25., 26., 27., 28., 29.],
                   [30., 31., 32., 33., 34., 35., 36., 37., 38., 39.]])

x2 = torch.tensor([[20., 21., 22., 23., 24., 25., 26., 27., 28., 29.],
                   [30., 31., 32., 33., 34., 35., 36., 37., 38., 39.],
                   [40., 41., 42., 43., 44., 45., 46., 47., 48., 49.],
                   [50., 51., 52., 53., 54., 55., 56., 57., 58., 59.]])

loss = simclr_nt_xent_loss(x1, x2, temperature=0.13)
print(loss)
