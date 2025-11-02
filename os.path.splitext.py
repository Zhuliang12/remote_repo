# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/11 16:55

'''
用于分割目录与文件名，返回分割后的文件与扩展名
'''

import os
from os.path import splitext

'''
print('嗨客网(www.haicoder.net)')
splitext = splitext('haicoder.txt')
print('splitext=', splitext)
splitext=splitext("D:")
print('splitext:',splitext)
splitext = splitext("C:\haicoder\haicoder.txt")
print('splitext:', splitext)
splitext = splitext('C:\haicoder\haicoder\haicoder')
print('splitext:', splitext)
'''

from PIL import Image
import numpy as np

ext = splitext('person.py')[1]
if ext == 'npy':  # .npy是numpy文件专用的二进制文件
    ext = Image.fromarray(np.load('person.py'))
    print(ext)
else:
    print(0)


def load_text(filename):
    pass


a = 13.5
b = 2
print(a // 2)  # 取整除的数据  # 6
