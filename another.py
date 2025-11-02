# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/18 15:13

import numpy as np
import torch
import torch.nn as nn
import xlrd  # 对excel文件的读取
import xlwt  # 对excel文件的写
import os

# print(torch.version.cuda)

'''
将txt文件导入excel文件，方便后续处理
'''

f = open('C:/Users/liang/Desktop/毕业相关/results/ori_data/0.886_0.7NWD/results (0.7NWD).txt', 'r', encoding='ANSI')  # 已只读模式打开txt文件，这里的编码模式为ANSI,后续打开excel文件也需要已该编码模式打开
wb = xlwt.Workbook(encoding='ANSI')  # 打开一个excel文件
ws1 = wb.add_sheet('first')  # 添加一个新表
row = 0  # 写入的起始行
col = 0  # 写入的起始列
k = 0
for lines in f:
    a = lines.split()
    k += 1
    for i in range(len(a)):
        ws1.write(row, col, a[i])  # 向Excel文件中写入每一项
        col += 1
    row += 1
    col = 0
wb.save('C:/Users/liang/Desktop/毕业相关/results/ori_data/0.886_0.7NWD/results (0.7NWD).xls')
