# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/12 14:51

'''
np.interp(x,xp,fp) 以xp,fp画线，返回x的值在这条线上对应的y的值
x: 要插入数据的x坐标
xp: 要拟合的数组的横坐标
fp: 要拟合的数组的纵坐标
一维线性插值
'''

import numpy as np
import matplotlib.pyplot as plt

px = np.linspace(0, 1, 1000)
x = [0, 1, 1.5, 2.72, 3.14]
xp = [1, 2, 3]
fp = [3, 2, 0]

y = np.interp(x, xp, fp)  # 得到一个列表
ap = np.trapz(y, x)  # 计算积分
print(ap)
print(type(y), y)
plt.plot(xp, fp, '-o')  # 显示插值出的曲线
plt.plot(x, y, 'x')  # 显示要插值的点在曲线上的位置
plt.show()
