# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/6 14:06
'''
标签版：
通过一定的索引的将文件划分成两个部分，
避免了的长时间的往下拖的导致的失误
'''
import os
import shutil

tagdir = r'C:/Users/liang/Desktop/mydata/stervel/Unet_labels'  # 要处理的目标文件夹
new_dir = r"C:/Users/liang/Desktop/yolo/DongBei  university/yolo_test/labels"  # 要放到的目标文件夹
filesname = os.listdir(tagdir)  # 获得该目录下所有的文件索引
start = int(1662)  # 填入需要切片的开头
end = int(5370)  # 切片的结尾
# print(filesname[1662:5370])
tagfile = '.json'
new_filelist = filesname[start:end]
print(new_filelist)
for name in new_filelist:
    fulldir = os.path.join(tagdir, name)
    print(fulldir)
    if tagfile in os.path.split(fulldir)[1]:
        print(fulldir)
        if os.path.isfile(fulldir):
            shutil.copy(fulldir, new_dir)
