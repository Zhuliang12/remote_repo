# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/12 13:52

'''
torch.utils.data.DataLoader
对数据进行batch的划分
把训练数据分成多个小组，每次抛出一组数据，直至把所有数据都抛出
positive:可以快速迭代数据
'''

import torch
from torch.utils.data import DataLoader, TensorDataset

BATCH_SIZE_1 = 5  # 这里一个批次是5个
BATCH_SIZE_2 = 4

x = torch.linspace(1, 10, 10)  # 训练数据
# torch.linspace(start,end,number)
# 从1开始到10，生成10个数据
print(x)
# tensor([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
y = torch.linspace(10, 1, 10)  # 标签
print(y)

# 将训练数据放入 DataLoader
torch_dataset = TensorDataset(x, y)  # 对于给定的tensor数据，将其变成dataset
print(torch_dataset)
# <torch.utils.data.dataset.TensorDataset object at 0x000002A91DB27A48>

loader1 = DataLoader(
    # 从数据库中每次抽出batch_size个样本
    dataset=torch_dataset,  # tensorDataset format
    batch_size=BATCH_SIZE_1,  # mini batch size
    shuffle=True,  # 要不要打乱数据（打乱比较好）
    num_workers=0  # 多线程读取数据 windows系统不支持num_workers >0
)


def show_batch_1():  # 展示
    for epoch in range(3):
        for step, (batch_x, batch_y) in enumerate(loader1):
            # training
            print("step:{},batch_x:{},batch_y:{}".format(step, batch_x, batch_y))


show_batch_1()  # 显示batch
'''
step:0,batch_x:tensor([ 2., 10.,  5.,  9.,  3.]),batch_y:tensor([9., 1., 6., 2., 8.])
step:1,batch_x:tensor([6., 7., 8., 1., 4.]),batch_y:tensor([ 5.,  4.,  3., 10.,  7.])
step:0,batch_x:tensor([3., 2., 1., 7., 6.]),batch_y:tensor([ 8.,  9., 10.,  4.,  5.])
step:1,batch_x:tensor([ 5.,  8.,  9.,  4., 10.]),batch_y:tensor([6., 3., 2., 7., 1.])
step:0,batch_x:tensor([ 5.,  4., 10.,  8.,  6.]),batch_y:tensor([6., 7., 1., 3., 5.])
step:1,batch_x:tensor([2., 3., 9., 1., 7.]),batch_y:tensor([ 9.,  8.,  2., 10.,  4.])
'''

loader2 = DataLoader(  # 将批次的变成4
    dataset=torch_dataset,
    batch_size=BATCH_SIZE_2,
    shuffle=True,
    num_workers=0
)


def show_batch_2():
    for epoch in range(3):
        for step, (batch_x, batch_y) in enumerate(loader2):
            print('step:{},batch_x:{},batch_y:{}'.format(step, batch_x, batch_y))


show_batch_2()
'''
step:0,batch_x:tensor([2., 3., 8., 9.]),batch_y:tensor([9., 8., 3., 2.])
step:1,batch_x:tensor([10.,  6.,  5.,  7.]),batch_y:tensor([1., 5., 6., 4.])
step:2,batch_x:tensor([1., 4.]),batch_y:tensor([10.,  7.])
step:0,batch_x:tensor([ 1.,  3., 10.,  9.]),batch_y:tensor([10.,  8.,  1.,  2.])
step:1,batch_x:tensor([2., 4., 6., 8.]),batch_y:tensor([9., 7., 5., 3.])
step:2,batch_x:tensor([5., 7.]),batch_y:tensor([6., 4.])
step:0,batch_x:tensor([8., 1., 6., 7.]),batch_y:tensor([ 3., 10.,  5.,  4.])
step:1,batch_x:tensor([ 4.,  5., 10.,  2.]),batch_y:tensor([7., 6., 1., 9.])
step:2,batch_x:tensor([9., 3.]),batch_y:tensor([2., 8.])
'''
