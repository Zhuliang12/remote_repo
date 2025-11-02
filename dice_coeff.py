# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/12 16:06

import torch
from torch import Tensor

tensor1 = torch.randn([2, 3, 4])
tensor2 = torch.randn([2, 3, 4])

print(tensor1, '\n', tensor2)

'''
def dice_coeff(input: Tensor, target: Tensor, reduce_batch_first: bool = True, eps: float = 1e-4):
    assert input.size() == target.size()
    assert input.dim() == 3 or not reduce_batch_first

    sum_dim = (-1, -2) if input.dim == 2 or not reduce_batch_first else (-1, -2, -3)

    inter = 2 * (input * target).sum(dim=sum_dim)
    sets_sum = input.sum(dim=sum_dim) + target.sum(dim=sum_dim)
    sets_sum = torch.where(sets_sum == 0, inter, sets_sum)

    dice = (inter + eps) / (sets_sum + eps)
    return dice


print(dice_coeff(tensor1, tensor2))
'''
tensor3 = torch.ones([2, 2, 2])
print(tensor3)
print(tensor1*tensor2)
# 每个元素对应相乘
sum_dim = (-1, -2, -3)
print(tensor3.sum(dim=sum_dim))
