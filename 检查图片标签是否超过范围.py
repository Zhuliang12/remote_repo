# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/11 22:50

'''
这个文件是为了检查，图片的标签是否超过了范围
'''

import os
import numpy as np

txt_filename = r"C:/Users/liang/Desktop/ori_data/labels/train/"
filesname = os.listdir(txt_filename)
# print(filesname)
for name in filesname:
    f = open("C:/Users/liang/Desktop/ori_data/labels/train/" + name, "r",
             encoding='utf-8',
             errors='ignore')
    for line in f:
        a = line.split(' ')[0]
        # print(name,a)

        if int(float(a)) >= 4:
            print(name, a)

        continue
# print(name)
