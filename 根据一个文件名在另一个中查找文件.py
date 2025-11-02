# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/6 13:25

import os
import shutil
import numpy as np

'''
写在前面：
全部为绝对路径
ori_path表示为original_path 要处理的文件的绝对路径
goa_path表示为 goal_path 为要使用的文件 绝对路径
new_path表示为 要移动的新文件路径
'''
ori_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\cropL_image/'
goa_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\labels/'
new_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\train/'
if not os.path.exists(new_path):
    os.makedirs(new_path)
filesname = os.listdir(goa_path)  # 获取了所有文件下的文件名  使用os.listdir的顺序是乱序
# filesname.sort()
tagfile = '.png'
# print(filesname)

for name in filesname:
    # print(name)1
    # print(str(name).split('.')[0][0:7])
    # name = str(name)[:-4] + str(tagfile)  # 这边要注意名字中存在点的文件
    name = str(name).split('.')[0] + str(tagfile)
    # print(name)
    fullpath = os.path.join(ori_path, name)
    # print(fullpath)
    if os.path.isfile(fullpath):
        # continue
        shutil.move(fullpath, new_path)
    else:
        print('未找到：', fullpath)

print('finished!!')
