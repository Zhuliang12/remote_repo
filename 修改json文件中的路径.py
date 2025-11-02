#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/7/9 11:27

# 本文件是为了json文件中未加载图片信息的时候需要修改json文件中的路径
# 使得json文件可以加载出来。
'''
要修改的位置：ipath的后缀，所转换的图片的后缀
json_path:json文件的路径
imagePath:图片存储路径
'''

import json
import pathlib


def json_path_change(json_path, image_path):
    json_path = pathlib.Path(json_path).expanduser().resolve()
    image_path = pathlib.Path(image_path).expanduser().resolve()
    print(f"Processing directory:{json_path}")

    for cnt, file in enumerate(json_path.iterdir()):
        print(f'{cnt= }')
        if file.suffix in ['.json']:
            print(f'Processing file: {file.name}')
            # raise ValueError('debug')
            # file_dir = json_path + name
            try:
                with file.open('r', encoding='utf-8') as f:
                    old_data = json.load(f)
                iPath = file.stem + '.png'
                img_path = image_path / iPath
                # old_data['imageData'] = None  # 这行代码可以在json文件中打出null
                # print(jpg_path)
                # raise ValueError('debug')
                old_data['imagePath'] = str(img_path)

                with file.open('w', encoding='gb18030') as f:
                    json.dump(old_data, f, ensure_ascii=False, indent=4)

                print('Update successful')
            except Exception as e:
                print(f'Error processing file {file.name}: {e}')

            print('ok')


if __name__ == '__main__':
    json_path = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\labels/'
    imagePath = r'E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\train/'
    json_path_change(json_path, imagePath)
    print('处理完成')
