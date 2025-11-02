# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/15 18:16

'''
1、寻找一个文件夹中所有相同后缀名的文件
2、将这些文件给剪切出去
'''

import os
import numpy as np
import shutil

original_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\train/'
goal_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\other/'
if not os.path.exists(goal_path):
    os.makedirs(goal_path)  # 如果不存在路径，就创建路径

all_file_name = os.listdir(original_path)


# print(all_file_name)
def search_sameSuffix_file(dirPath, suffix):  # 获得文件中的所有相同后缀名的文件
    dirs = os.listdir(dirPath)
    for currentFile in dirs:
        fullPath = dirPath + '/' + currentFile
        if currentFile.split('.')[-1] == suffix:
            if os.path.isfile(fullPath):  # 找到要剪切的目标
                shutil.move(fullPath, goal_path)  # 原目录，到新目录

            print(fullPath)


dirpath = original_path
suffix = 'json'
search_sameSuffix_file(dirpath, suffix)
