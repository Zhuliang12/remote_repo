# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/23 15:22

import os

path = r'D:\panel\lodge/'  # 首先定义文件夹的路径
save_path = r'D:\panel\lodging/'
if not os.path.exists(save_path):
    os.makedirs(save_path)
file_names = os.listdir(path)  # 创建一个所有文件名的列表
# file_names.sort(key=lambda x: int(x[13:-4]))  # 通过切片对其进行排序 需要对其排序
print(file_names)

i = 1  # 设置开始的序号
for name in file_names:
    i = int(i)
    if i < 10:
        i = '' + str(i)
    elif 10 <= i and i < 100:
        i = '' + str(i)
    elif 100 <= i and i < 1000:
        i = '' + str(i)
    elif 1000 <= i and i < 10000:
        i = '' + str(i)
    else:
        i = '' + str(i)  # 001，002,，003......的循环，我比较喜欢采取这种方式命名
    photo_name = str(name).split('.')[0]
    # 我整理照片，photo_name是指文件不含.jpg的名字，split('.')字符按.划分成两个，[0]前[1]后
    # photo_format = str(name).split('.')[1]
    photo_format = '.jpg'
    name_prefix = 'lodge'
    new_name = name_prefix + '_' + i + photo_format  # 新名字加上序号
    os.rename(os.path.join(path, name), os.path.join(save_path, new_name))  # 执行重命名
    i = int(i) + 1
