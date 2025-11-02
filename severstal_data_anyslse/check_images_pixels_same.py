# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/25 19:22

'''
数据集分析
查看数据图片的每一个通道的像素值是否都相同
'''
import os
import numpy as np
import cv2 as cv

datasets_path = 'D:/mydata/stervel/original_data/no_class_images/no_images/'
filesname = os.listdir(datasets_path)
# print(filesname)
for i in filesname:
    file_path = str(datasets_path + str(i))
    # print(file_path)
    img = cv.imread(file_path)
    a1 = img[:, :, 0]
    a2 = img[:, :, 1]
    a3 = img[:, :, 2]
    if (a1 == a2).all() and (a1 == a2).all() and (a2 == a3).all():
        print('%s is improved' % format(i))
    else:
        print('%s is not improved' % format(i))
