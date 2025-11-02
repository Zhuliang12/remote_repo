#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/9/27 15:42

import pathlib
import json
from PIL import Image


def get_json_boundingbox(one_txt, width, height):
    with open(one_txt, 'r', encoding='utf-8') as txt_labels:
        print(f'{txt_labels= }')
        # lines = txt_labels.readlines()
        for line in txt_labels:
            label, center_x, center_y, Width, Height = line.split()
            print(f'{float(center_x)= }')
            x_min = (float(center_x) - (float(Width) / 2)) * width
            x_max = (float(center_x) + (float(Width) / 2)) * width
            y_min = (float(center_y) - (float(Height) / 2)) * height
            y_max = (float(center_y) + (float(Height) / 2)) * height

    return label, x_min, x_max, y_min, y_max


def txt__json(txt_dir, image_dir, json_dir, class_list, suffix):
    txt_path = pathlib.Path(txt_dir).expanduser().resolve()
    json_path = pathlib.Path(json_dir).expanduser().resolve()
    if not json_path.exists():
        json_path.mkdir()
    # print(txt_path)
    for one_txt in txt_path.iterdir():
        if one_txt.suffix == '.txt':
            image_name = one_txt.name.split('.')[0] + suffix
            image_file_dir = image_dir + image_name
            json_name = one_txt.name.split('.')[0] + '.json'
            json_file_dir = json_dir + json_name
            try:
                with Image.open(image_file_dir) as img:
                    width, height = img.size
                    # 构建目标检测的JSON结构
                    detection_data = {
                        'version': "5.2.0.post4",
                        'flags': {},
                        'shapes': [],
                        'imagePath': image_file_dir,
                        'imageData': None,
                        'imageHeight': height,
                        'imageWidth': width,
                    }
                label, x_min, x_max, y_min, y_max = get_json_boundingbox(one_txt, width, height)
                # with open(one_txt, 'r', encoding='utf-8') as txt_labels:
                #     print(f'{txt_labels= }')
                #     # lines = txt_labels.readlines()
                #     for line in txt_labels:
                #         label, center_x, center_y, Width, Height = line.split()
                #         print(f'{float(center_x)= }')
                #         x_min = (float(center_x) - (float(Width) / 2)) * width
                #         x_max = (float(center_x) + (float(Width) / 2)) * width
                #         y_min = (float(center_y) - (float(Height) / 2)) * height
                #         y_max = (float(center_x) + (float(Height) / 2)) * height

                detection_data['shapes'].append({
                    'label': class_list[int(label)],
                    'points': [[x_min, y_min], [x_max, y_max]],
                    "group_id": None,
                    'description': None,
                    'shape_type': "rectangle",
                    'flags': {}
                })
                # center_x = line.split(' ')[1]
                # center_y = line.split(' ')[2]
                # Width = line.split(' ')[3]
                # Height = line.split(' ')[4]
                # label = line.split(' ')[0]
                # print(f'{label= } {type(label)= } {center_x= }')
                # print(f'{line= }')

                with open(json_file_dir, 'w') as f:
                    json.dump(detection_data, f, indent=4)

            except Exception as e:
                print(e)

            print(f'{image_file_dir= }')
            print(f'{json_file_dir= }')


if __name__ == '__main__':
    class_list = ['bird']  # 标签列表
    txt_dir = r'E:\zhuliang\xunjian\tryout\src\runs\detect\predict12\labels/'  # txt文件路径
    image_dir = r'C:\Users\liang\Desktop\bird_images/'  # 对应的图片路径
    json_dir = r'C:\Users\liang\Desktop\bird_json/'  # 要存储的json路径
    image_suffix = '.jpg'  # 图片的后缀
    txt__json(txt_dir, image_dir, json_dir, class_list, image_suffix)
