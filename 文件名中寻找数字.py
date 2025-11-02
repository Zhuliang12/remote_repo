# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/3 21:54

'''
获取文件名中的数字，可以通过切片的方式获得数字
'''
import os
import numpy as np

path='D:/mydata/stervel/original_data/class_2_images/2_images/'
path_list=os.listdir(path)
# print(path_list)
for parent, dirnames, filenames in os.walk(path):
    for name in filenames:
        number=int(name[13:-4])
        print(number)

