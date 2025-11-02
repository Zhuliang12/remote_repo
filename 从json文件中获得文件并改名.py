# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/3 22:40
'''
通过json文件获得图片获得图像的复制
'''
import os
import shutil
import json

json_path = 'D:/mydata/stervel/original_data/class_2_images/2_json/'
jpg_path = 'D:/mydata/stervel/original_data/train_images/'
img_path = 'D:/mydata/stervel/original_data/class_2_images/2_images/'

list_json = os.listdir(json_path)
list_json.sort(key=lambda x: int(x[13:-5]))

for cnt, json_name in enumerate(list_json):
    json_file = json_path + json_name
    index = int(cnt + 1)
    with open(json_file, 'r', encoding='gb18030') as path_json:
        jsonx = json.load(path_json)
        image_name_path = jsonx['imagePath']
        image_name = image_name_path.split("\\")[-1]
        jpg_p = jpg_path + image_name  # 获得数据路径
        photo_name = str(image_name).split('.')[0]
        photo_format = str(image_name).split('.')[1]
        new_name = 'burying_slag_' + str(index) + '.' + photo_format
        if os.path.isfile(jpg_p):
            shutil.copy(jpg_p, img_path)
            os.rename(os.path.join(img_path, image_name), os.path.join(img_path, new_name))
