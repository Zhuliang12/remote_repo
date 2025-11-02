#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/7/17 17:54
'''
这个代码是为了生成空的json文件，为了没有标签的图像获得json文件
'''
import numpy as np
import os
import cv2
import base64
import json


def main():
    img_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\feature_true/'
    save_json_add = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\json/'
    imagelist = os.listdir(img_path)
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imdecode(np.fromfile(img_file, dtype=np.uint8), cv2.IMREAD_COLOR)
        print(img_file)
        height, width, channel = img.shape
        j = {
            "version": "4.5.6",
            "flags": {},
            "shapes": [],
            "imagePath": "{}.jpg".format(image_pre),
            "imageData": None,
            "imageHeight": height,
            "imageWidth": width
        }
        if not os.path.exists(save_json_add):
            os.makedirs(save_json_add)
        json_path = save_json_add + image_pre + '.json'
        with open(json_path, 'w') as f:
            json.dump(j, f, indent=6)
        print('json_success')


if __name__ == '__main__':
    main()
