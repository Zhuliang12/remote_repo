# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/6/3 14:58
'''
这个文件是为了解决使用椒盐噪声从而导致的txt文件的复制与重命名

'''

import os


def copy_txt(label,save_path,save_name):
    txt_path=save_path+save_name
    with open(txt_path,'w+') as file:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_strxy = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
            new_strxy = label + ' ' + new_strxy
            file.writelines(new_strxy + '\n')


txt_path=r'C:/Users/liang/Desktop/ori_data/labels/4/'
save_path=r'C:/Users/liang/Desktop/ori_data/labels/test/'
filenames=os.listdir(txt_path)
for filename in filenames:
    new_filename=filename.split('.')[0]+'_SP.txt'
    label_path=txt_path+filename
    copy_txt(label_path,save_path,new_filename)
    print(filename)
