# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/14 19:06

'''
这个是为了计算每一类共有多少个缺陷
'''
import os
import numpy as np
import pathlib

class_0 = 0
class_1 = 0
class_2 = 0
class_3 = 0
txt_filename = r"D:\mydata\ori_data\train_images\400x256_all\labels\valid/"
txt_path = pathlib.Path(txt_filename).expanduser().resolve()

# print(filesname)
for cnt, name in enumerate(txt_path.iterdir()):
    if name.suffix in ['.txt']:
        f = open(txt_filename+os.sep + name.stem + name.suffix, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            line = line.strip()
            a = line.split(' ')[0]
            print(name, a)
            if int(a) == 0:
                class_0 += 1

            elif int(a) == 1:
                class_1 += 1
            elif int(a) == 2:
                class_2 += 1
            elif int(a) == 3:
                class_3 += 1
                continue
print('class_0=', class_0)
print('class_1=', class_1)
print('class_2=', class_2)
print('class_3=', class_3)
