# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/26 16:36

'''
获得目标像素值范围，大小查看像素在输入过程中的
'''
import os
import json
import numpy as np
import shutil

small = 0
relatively_small = 0
less = 0
middle = 0
big = 0
large = 0

low_wh_rate = 0
middle_wh_rate = 0
high_wh_rate = 0
max_piexls = 0

txt_path = 'D:/mydata/ori_data/train_images/txt/'
list_txt = os.listdir(txt_path)
for name in list_txt:
    with open(txt_path + os.sep + name, "r") as f:
        lines = f.readlines()
        for line in lines:
            # 输出数组的维度
            # print(arr.shape[0])
            print(name, line)
            w = line.split(" ")[3]
            h = line.split(" ")[4]
            num_pixels = np.round((float(w) * float(h)) * 409600 + 0.15)
            if max_piexls < num_pixels:
                max_piexls = num_pixels

            # print(name, num_pixels)
            # pixel_rate = float(num_pixels / 409600)

            # wh_rate = '%.6f' % float(float(w) / float(h))
            # # print(name, wh_rate)
            # # if float(wh_rate) < 0.5 and float(num_pixels) <= 2056:
            # if float(wh_rate) < 0.5:
            #     low_wh_rate += 1
            # elif 0.5 < float(wh_rate) < 2:  # and 6063 >= float(num_pixels) > 2056:
            #     middle_wh_rate += 1
            # elif float(wh_rate) > 2.0:  # and float(num_pixels) > 6063:
            #     high_wh_rate += 1

            if float(num_pixels) <= 1024:
                small += 1
            elif 4096 >= float(num_pixels) > 1024:
                less += 1
            elif 20480 >= float(num_pixels) > 4096:
                relatively_small += 1
            elif 40960 >= float(num_pixels) > 20480:
                middle += 1
            elif 102400 >= float(num_pixels) > 40960:
                big += 1
            elif float(num_pixels) > 102400:
                large += 1

# print('small<0.005 =', small)
# print('less>0.005 =', less)
# print('relatively_small>0.01 =', relatively_small)
# print('middle>0.1 =', middle)
# print('big>0.25 =', big)
# print('large>0.4 =', large)

print('low_wh_rate=', low_wh_rate)
print('middle_wh_rate=', middle_wh_rate)
print('high_wh_rate=', high_wh_rate)

# print(max_piexls)
