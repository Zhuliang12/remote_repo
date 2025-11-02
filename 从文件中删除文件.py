# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/11 20:44

import os
import shutil

image_path = 'D:/mydata/stervel/empty'
goal_path = 'D:/mydata/stervel/seversatl_data/images/test'
move_path = 'D:/mydata/stervel/other'
name = os.listdir(image_path)
# print(name)
for i in name:
    path = os.path.join(goal_path, i)
    ori_path = os.path.join(image_path, i)
    print(path)
    if os.path.isfile(path):
        shutil.move(ori_path, move_path)
