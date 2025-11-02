# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/11 18:49

import os
import shutil
import numpy as np

txt_filename = 'D:/mydata/stervel/empty.txt'
image_path = 'D:/mydata/stervel/seversatl_data/images/valid'
save_path = 'D:/mydata/stervel/empty'
prefix = 'skin_scale_'
file = '.jpg'
f = open(txt_filename, 'r', encoding='utf-8', errors='ignore')
for line in f:
    a = line.strip('\n')
    number = a
    name = prefix + number + file
    # print(a)

    img_p = os.path.join(image_path, name)
    print(img_p)
    if os.path.isfile(img_p):
        shutil.copy(img_p, save_path)
