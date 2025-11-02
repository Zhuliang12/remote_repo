# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/11 18:17

'''
这个文件是一个npy文件
.npy文件是numpy专用的二级制文件
'''

import numpy as np

# 写进 npy文件
a = np.arange(5)
# print(a)
# np.save()和np.load() 是读写磁盘数组数据的两个主要函数
np.save('text.npy', a)  # 这就生成了一个.npy文件

# 读取 npy文件
test = np.load('text.npy', encoding='latin1')  # 加载文件
# print(test)
print(type(test))  # 查看数据类型
# <class 'numpy.ndarray'>

# 写入txt文件
# 将numpy的矩阵数据存入txt文件

doc = open("npy.txt", 'a')  # 打开一个存储文件 并依次写入
for i in range(len(test)):
    doc.write(str(test[i]) + ' ')
doc.close()




