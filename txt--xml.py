# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/15 14:38

import time
import os
from PIL import Image
import cv2
import numpy as np

'''人为构造xml文件的格式'''
out0 = '''<annotation>
    <folder>%(folder)s</folder>
    <filename>%(name)s</filename>
    <path>%(path)s</path>
    <source>
        <database>None</database>
    </source>
    <size>
        <width>%(width)d</width>
        <height>%(height)d</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
'''
out1 = '''    <object>
        <name>%(class)s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%(xmin)d</xmin>
            <ymin>%(ymin)d</ymin>
            <xmax>%(xmax)d</xmax>
            <ymax>%(ymax)d</ymax>
        </bndbox>
    </object>
'''

out2 = '''</annotation>
'''

'''txt转xml函数'''


def translate(fdir, lists):
    source = {}
    label = {}
    for jpg in lists:
        print(jpg)
        if jpg[-4:] == '.jpg':
            image = cv2.imread(jpg)  # 路径不能有中文
            h, w, _ = image.shape  # 图片大小
            #            cv2.imshow('1',image)
            #            cv2.waitKey(1000)
            #            cv2.destroyAllWindows()
            #####
            fxml = jpg.replace('.jpg', '.xml')  # 将路径改为xml文件
            fxml = open(fxml, 'w')  # 以读写的方式打开xml文件
            imgfile = jpg.split('/')[-1]
            source['name'] = imgfile
            source['path'] = jpg
            source['folder'] = os.path.basename(fdir)

            source['width'] = int(w)
            source['height'] = int(h)

            fxml.write(out0 % source)  # 写完第一段代码
            ####### 上面是操作图片
            txt = jpg.replace('.jpg', '.txt')
            # 增加判断这个文件是不是空的
            if not os.path.getsize(txt):
                print(txt, 'is empty')
            else:
                with open(txt, "r", encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        line = line.strip()
                        a = line.split(' ')[1]
                        b = line.split(' ')[3]
                        c = line.split(' ')[2]
                        d = line.split(' ')[4]
                        '''把txt上的数字（归一化）转成xml上框的坐标'''
                        xmin = float(float(a) - 0.5 * float(b)) * int(w)
                        ymin = float(float(c) - 0.5 * float(d)) * int(h)
                        xmax = float(xmin + float(b) * w)
                        ymax = float(ymin + float(d) * h)

                        '''把txt上的第一列（类别）转成xml上的类别
                                               我这里是labelimg标1、2、3，对应txt上面的0、1、2'''
                        class_list = ['Frp', 'Sr', 'Ss', 'Ox']
                        class_id = int(float(line.split(' ')[0]))
                        label['class'] = str(class_list[class_id])  # 类别索引从1开始

                        label['xmin'] = xmin
                        label['ymin'] = ymin
                        label['xmax'] = xmax
                        label['ymax'] = ymax

                        fxml.write(out1 % label)

                    # if label['xmin']>=w or label['ymin']>=h or label['xmax']>=w or label['ymax']>=h:
                    #     continue
                    # if label['xmin']<0 or label['ymin']<0 or label['xmax']<0 or label['ymax']<0:
                    #     continue

                fxml.write(out2)


if __name__ == '__main__':
    file_dir = r'C:\Users\liang\Desktop\ori_data\images\400x256_all\labels\all/'  #
    lists = []
    for i in os.listdir(file_dir):
        if i[-3:] == 'jpg':
            lists.append(file_dir + '/' + i)
            # print(lists)
    translate(file_dir, lists)
    print('---------------Done!!!--------------')
