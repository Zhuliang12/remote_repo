# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/16 14:25

'''
获得一个文件夹下所有文件的文件名
如果是n个后缀 file_name下写[0：-(n+1)]

'''
import os

path = r"C:\Users\liang\Desktop\ori_data\images\400x256_all\labels/images/"  # 要提取名字的文件路径
file_name_list = os.listdir(path)

with open(r'C:\Users\liang\Desktop\ori_data\images\400x256_all\labels/train.txt', 'w') as f:
    # 要存放到的路径
    for file_name in file_name_list:
        f.write(file_name[0:-4] + '\n')  # -5表示从后往前数，到小数点位置
