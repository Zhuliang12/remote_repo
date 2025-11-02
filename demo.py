# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/12 13:28

import torch
import numpy as np

'''
a = torch.rand(5, 5)
b = np.ones_like(a)
c = np.ndarray(shape=(5, 5))
# print(c)
print(b)
w = [0.0, 0.0, 0.1, 0.9]
# print(type(w), type(a))
# print(a, '\n', a[:, :4], '\n', a[:4])
# print(type(w), type(b))
print((b[:, :4] * w).sum(1))
print('b[:,4]=', b[:, :4])

a = np.array([0, 1, 0, 1])
c1 = np.concatenate(([0.], a, [a[-1] + 0.01]))
'''
c = np.array([[0, 1, 0, 1, 1.5],
              [1, 0, 1, 0, 1.2]])  # (2,5)
c = torch.tensor(c)
# print(a.shape, c.shape)
print(c)
x = torch.where(c >= 1.)
print('x=', x)  # 获得高于阈值的坐标
print('x[0].shape[0]', x[0].shape[0])  # x[0].shape[0] 6
print('torch.stack(x,1)=', torch.stack(x, 1))
print(c[x[0], x[1]])  # 获取所有的符合阈值的值
print(c[x[0], x[1]][:None])  # 将其变成列向量
matches = torch.cat((torch.stack(x, 1), c[x[0], x[1]][:, None]), 1).cpu().numpy()
# 获得 对应坐标和对应的阈值

print('matches=', matches, matches.shape)

'''
i = np.array([True, False, False, True])
b = a.cumsum(0)  # 按行求累积和
# b = a[i]
print(b)

px = np.linspace(0, 1, 1000, retstep=True)
# print(px)
'''
'''
recall = np.array([0.1, 0.4, 0.2, 0.3, 0.4])
final_1 = np.flip(np.maximum.accumulate(np.flip(recall)))
final_2 = np.flip(np.maximum.accumulate(recall))
final_3 = np.flip(recall)
final_4 = np.maximum.accumulate(final_3)
final_5=np.maximum.accumulate(recall)
print(final_1)
print(final_2)
print(final_3)
print(final_4)
print(final_5)
'''
