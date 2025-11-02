# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/3 13:17
# 更新时间 2023，07，06

# 更新了，要输入所转图片的大小的bug, 使用只需要修改输入json路径和输出txt路径


import os
import pathlib

import numpy as np
import json

class_list = ['rice']
'''
def transformer(x1y1, x2y2):
    x1, y1 = x1y1[0], x2y2[1]
    x2, y2 = x2y2[0], x2y2[1]
    x_max = max(x1, x2)
    x_min = min(x1, x2)
    y_max = max(y1, y2)
    y_min = min(y1, y2)
    x = (x_max + x_min) / 3200
    y = (y_max + y_min) / 512
    w = (x_max - x_min) / 1600
    h = (y_max - y_min) / 256
    return x, y, w, h
'''


def json2txt(path_json, path_txt):
    with open(path_json, 'r', encoding='gb18030') as path_json:
        jsonx = json.load(path_json)
        width = jsonx['imageWidth']
        height = jsonx['imageHeight']
        with open(path_txt, 'w+') as ftxt:
            for shape in jsonx['shapes']:
                x1y1, x2y2 = shape.get('points')
                x1, y1 = x1y1[0], x1y1[1]
                x2, y2 = x2y2[0], x2y2[1]
                x_max = max(x1, x2)
                x_min = min(x1, x2)
                y_max = max(y1, y2)
                y_min = min(y1, y2)
                x = '%.6f' % float((x_max + x_min) / (2 * float(width)))
                y = '%.6f' % float((y_max + y_min) / (2 * float(height)))
                w = '%.6f' % float((x_max - x_min) / float(width))
                h = '%.6f' % float((y_max - y_min) / float(height))
                # print(xy)
                label_id = str(class_list.index(shape.get('label')))
                if shape.get('label') not in class_list:
                    print("json=%s" % (path_json))
                    raise ValueError('the class is not in class_list')
                strxy = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
                strxy = label_id + ' ' + strxy
                ftxt.writelines(strxy + "\n")


if __name__ == '__main__':
    dir_json = r'F:\LT_DATASETS\PUBLIC\DATASET_ANIMAL_AND_BIRD\DETECTION\train\jsons/'
    dir_txt = r'F:\LT_DATASETS\PUBLIC\DATASET_ANIMAL_AND_BIRD\DETECTION\train\txt/'
    if not os.path.exists(dir_txt):
        os.makedirs(dir_txt)  # 如果没有txt文件，创建一个txt文件
    json_path = pathlib.Path(dir_json).expanduser().resolve()

    # list_json = os.listdir(dir_json)
    for cnt, name in enumerate(json_path.iterdir()):
        if name.suffix in ['.json']:
            print('cnt=%d,name=%s' % (cnt, name))
            # path_json = dir_json + name
            path_txt = dir_txt + name.stem + '.txt'
            # print(path_json, path_txt)
            json2txt(name, path_txt)
