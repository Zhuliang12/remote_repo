# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/16 11:57
'''
打开txt文件，判断是否为空，如果为空则跳过
如果不为空，将其剪切到一个新的文件夹中
'''

import os
import numpy as np
import shutil

old_dir = 'D:/mydata/stervel/train/images_labels_all_rec/txt_labels_all/'
new_dir = 'D:/mydata/stervel/train/images_labels_all_rec/txt_labels/'
txt_name = os.listdir(old_dir)  # 获得所有的txt文件名称

for name in txt_name:
    full_path = old_dir + '/' + name
    # print(full_path)
    if not os.path.getsize(full_path):
        print(full_path, 'is empty')
    else:
        print(full_path, 'is ok')
        if os.path.isfile(full_path):
            shutil.move(full_path, new_dir)
