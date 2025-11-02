# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/12 20:24

'''
numpy.unique(arr,return_index,return_inverse,return_counts)
arr: 输入数组 如果不是一维数组会将其展开
return_index；if true  返回新列表元素在旧列表中的位置 下表
return_inverse: if true  返回旧列表元素在新列表中位置 下标
return_counts: if true  返回去重数组中元素在原始数组出现次数
'''

import numpy as np

import numpy as np

A = [1, 2, 2, 5, 3, 4, 3]
a = np.unique(A)
print(a)
print("______")
# [1 2 3 4 5]


a, indices = np.unique(A, return_index=True)  # 返回新列表元素在旧列表中的位置（下标）
print(a)  # 列表
print(indices)  # 下标
print("______")
'''
[1 2 3 4 5]
[0 1 4 5 3]
'''

a, indices = np.unique(A, return_inverse=True)  # 旧列表的元素在新列表的位置
print(a)
print(indices)
print(a[indices])  # 使用下标重构原数组
print("______")

'''
[1 2 3 4 5]
[0 1 1 4 2 3 2]
[1 2 2 5 3 4 3]
'''
a, indices = np.unique(A, return_counts=True)  # 每个元素在旧列表里各自出现了几次
print(a)
print(indices)
print("______")
'''
[1 2 3 4 5]
[1 2 2 1 1]'''
B = ([1, 2], [2, 5], [3, 4])
b = np.unique(B)
C = ['fgfh', 'asd', 'fgfh', 'asdfds', 'wrh']
c = np.unique(C)
print(b)
print(c)

'''
[1 2 3 4 5]
['asd' 'asdfds' 'fgfh' 'wrh']
'''
