# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/5/26 17:03


'''
该文件可以json文件转换成适合YOLOv5实例分割中的标注文件
文件保存在YOLOv5_seg中的train,test,valid
'''

import os
import pathlib

import cv2
import json
import numpy as np


def txt_write(x, img_x, img_y, txt):
    data = x['points']
    n = 1
    for x in data:
        for i in x:
            if n % 2 == 0:
                txt.write(' ' + str(round(i / img_x, 6)))
                n += 1
            else:
                txt.write(' ' + str(round(i / img_y, 6)))
                n += 1
    txt.write('\n')


def json2txt(json_path, save_path):
    txt = open(save_path, 'w')
    with open(json_path, "r") as f:
        data = f.read()
    data = json.loads(data)
    img_x = data['imageHeight']
    img_y = data['imageWidth']
    shapes = data['shapes']
    label_dict = {
        'burying_slag': '1',
        "furnace_roll_pimples": '0',
        "oxidation": '3',
        "skin_scale": '2'
    }
    for x in shapes:
        # print(x['label'])
        # 此处面向不同分类，需要改动下面的标签值，如果是多分类，那么需要增加新的if
        # 只是单分类的话，可以直接去掉if，把里面的模块拿出来用
        index = label_dict[x['label']]
        txt.write(index)
        # if x['label'] == 'burying_slag':
        #     txt.write('1')
        # elif x['label'] == "furnace_roll_pimples":
        #     txt.write("0")
        # elif x['label'] == "oxidation":
        #     txt.write("3")
        # elif x['label'] == "skin_scale":
        #     txt.write('2')
        txt_write(x, img_x, img_y, txt)
    txt.close()


# 单文件测试
# save_dir = "/workspace/" #文件路径
# name = 'test'
# save_path = save_dir + name + '.txt' # 也可以是.doc
# json_path = '/json/65161.json'
# json2txt(json_path,save_path)

# 文件夹
if __name__ == '__main__':
    json_dir = 'D:/mydata/stervel/Seversatl/labels/voc/valid_json'
    save_dir = 'C:/Users/liang/Desktop/myyolo/yolov5-seg-master/dataset/labels/valid'
    path_json = pathlib.Path(json_dir).expanduser().resolve()
    os.makedirs(save_dir, exist_ok=True)
    for cnt, file in enumerate(path_json.iterdir()):
        if file.suffix in ['.json']:
            print('cnt=%d,name=%s' % (cnt, file))
            json_path = json_dir + '/' + file.stem + '.json'
            save_path = save_dir + '/' + file.stem + '.txt'
            json2txt(json_path, save_path)
