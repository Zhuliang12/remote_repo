# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/5 19:48

# -*- coding:utf-8 -*-

# os模块中包含很多操作文件和目录的函数
import os

# 获取目标文件夹的路径(提供两种方法)
# 第一种方法：（适用于要被合并的文件的文件夹和该Python文件在同一目录下）
# meragefiledir = os.getcwd()+'\\11-21KeywordsTop' #这里的11-21KeywordsTop需要替换成自己的文件夹名字（文件夹里面是要合并的所有txt文件）
# 第二种方法：（适用于位置任意的情况，不要求同一目录下）
meragefiledir = 'C:/Users/liang/Desktop/yolo/DongBei  university/NEU-DEF/txt1'  # 这里的D:/A Project/11-21KeywordsTop需要替换成自己的文件夹的绝对路径哦

# 获取当前文件夹中的文件名称列表
filenames = os.listdir(meragefiledir)

# 打开当前目录下的result.txt文件，如果没有则创建
file = open('all.txt', 'w', encoding='utf8')  # 这里的keywords_1121_merge.txt就是我们的合并后的结果的txt的名字啦，名字随意改无所谓

# 向文件中写入字符
# 先遍历文件名
for filename in filenames:
    filepath = meragefiledir + '\\'
    filepath = filepath + filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding='utf8'):
        file.writelines(line)
    file.write('')
# 关闭文件
file.close()
