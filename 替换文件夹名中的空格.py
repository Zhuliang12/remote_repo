# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/4 21:11

import os

rootdir = r'E:/xunjian/2/outkills/'

img_file_l = []
img_dir_l = []

for parent, dirnames, filenames in os.walk(rootdir):
    for img_one in filenames:
        # old_name = img_one.split('/')[-1]
        # new_name=img_one+'.jpg'
        name = img_one[:-4]
        new_name = name.replace("_1", "")  +'.jpg'# 此处可以自行修改变成去除空格or去除逗号等等
        new_name = os.path.join(rootdir, new_name)
        old_name = os.path.join(rootdir, img_one)
        print(old_name)
        print(new_name)
        os.rename(old_name, new_name)
