# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/11/27 18:14
'''
csv格式转换为txt格式
'''

# 批量处理csv 保存为txt

import numpy as np
import glob
import os

path = r'C:\Users\liang\Desktop\缺陷数据集\谢 缺陷数据集'  # 需要导入的CSV文件路径
file = glob.glob(os.path.join(path, "*.csv"))  # 文件名相同部分，读取该文件夹下的所有csv文件名
# print(file) # ['C:\\Users\\liang\\Desktop\\缺陷数据集\\谢 缺陷数据集\\sample_submission.csv',
# 'C:\\Users\\liang\\Desktop\\缺陷数据集\\谢 缺陷数据集\\train.csv']

n = 0
for m in file:
    t1 = np.loadtxt(m, dtype=np.float,delimiter=',', encoding='utf-8')  # 读取csv文件内容为numpy数组
    t2 = np.corrcoef(t1, rowvar=0)  # 操作数据，这里是列相关
    n += 1  # n是要保存为txt文件名的变量
    np.savetxt('C:\\Users\\liang\\Desktop\\缺陷数据集\\谢 缺陷数据集\\corr\\3_AD00%d_ts.txt' % (n), t2)
    # 保存文件的路径名
y = np.loadtxt('C:\\Users\\liang\\Desktop\\缺陷数据集\\谢 缺陷数据集\\corr\\3_AD00%d_ts.txt')

print(y)
