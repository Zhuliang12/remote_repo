# yolov5 根据检测框和 xml 文件 裁减出 检测框,可以按照标记的类别数进行分类裁减，img 和 xml 文件数目 要一致， 不然会报错。
# 生成xml 的路径中，不能有中文，不然会报错。

import cv2
import xml.etree.ElementTree as ET
import numpy as np

import xml.dom.minidom
import os
import argparse


def main():
    # JPG文件的地址
    img_path = 'C:/Users/liang/Desktop/work/bridge_zone_02/'
    # XML文件的地址
    anno_path = 'C:/Users/liang/Desktop/work/new_xml/'
    # 存结果的文件夹

    cut_path = 'C:/Users/liang/Desktop/work/class/'
    # 获取文件夹中的文件
    imagelist = os.listdir(img_path)
    # print(imagelist
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imread(img_file)
        xml_file = anno_path + image_pre + '.xml'
        # DOMTree = xml.dom.minidom.parse(xml_file)
        # collection = DOMTree.documentElement
        #objects = collection.getElementsByTagName("object")

        tree = ET.parse(xml_file)
        print("image: ",image)
        root = tree.getroot()
        # if root.find('object') == None:
        #     return
        count = 0
        for obj in root.iter('object'):

            cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            print(image)
            b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text)]
            img_cut = img[b[1]:b[3], b[0]:b[2], :]
            path = os.path.join(cut_path, cls)
            # 目录是否存在,不存在则创建
            mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
            mkdirlambda(path)

            #cv2.imwrite(os.path.join(cut_path, cls, 'cut_img_{}.jpg'.format(image_pre)), img_cut)

            # cv2.imwrite(os.path.join(cut_path + cls + "/" + '%s_%s' % (image_pre, count) + ".png"), img_cut)
            cv2.imwrite(os.path.join(cut_path  + cls +   "/" + '%s' % (image_pre) +   ".png"), img_cut)


            #cv2.imwrite(img_path + '/' + '%s_%s' % (img_name, count) + '.jpg', obj_img)

            count += 1


            # for object in objects:
            #     print("start")
            #     name=object.getElementsByTagName('name')[0]
            #     # obj.find('name').text
            #     print(name)
            #     print(type(name))
            #
            #     bndbox = object.getElementsByTagName('bndbox')[0]
            #     xmin = bndbox.getElementsByTagName('xmin')[0]
            #     xmin_data = xmin.childNodes[0].data
            #     ymin = bndbox.getElementsByTagName('ymin')[0]
            #     ymin_data = ymin.childNodes[0].data
            #     xmax = bndbox.getElementsByTagName('xmax')[0]
            #     xmax_data = xmax.childNodes[0].data
            #     ymax = bndbox.getElementsByTagName('ymax')[0]
            #     ymax_data = ymax.childNodes[0].data
            #     xmin = int(xmin_data)
            #     xmax = int(xmax_data)
            #     ymin = int(ymin_data)
            #     ymax = int(ymax_data)
            #     img_cut = img[ymin:ymax, xmin:xmax, :]
            #     cv2.imwrite(cut_path + 'cut_img_{}.jpg'.format(image_pre), img_cut)
            #print("&&&&")


if __name__ == '__main__':
    main()
