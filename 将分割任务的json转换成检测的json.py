#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/8/18 22:43

# 将采用Label中多边形工具标注的用于语义分割的原始json文件转换成 用于目标检测的用矩形框标注的原始json文件
import json
import os
import pathlib


def convert_semantic_to_detection(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # 构建目标检测的JSON结构
    detection_data = {
        'version': "5.2.0.post4",
        'flags': {},
        'shapes': [],
        'imagePath': data['imagePath'],
        'imageData': None,
        'imageHeight': data['imageHeight'],
        'imageWidth': data['imageWidth'],
    }

    for shape in data['shapes']:
        # 转换多边形为矩形
        label = shape['label']
        points = shape['points']
        x_values = [point[0] for point in points]
        y_values = [point[1] for point in points]
        x_min = min(x_values)
        y_min = min(y_values)
        x_max = max(x_values)
        y_max = max(y_values)

        # 添加矩形边界框到目标形状列表
        detection_data['shapes'].append({
            'label': label,
            'points': [[x_min, y_min], [x_max, y_max]],
            "group_id": None,
            'description': None,
            'shape_type': "rectangle",
            'flags': {}
        })

    with open(output_file, 'w') as f:
        json.dump(detection_data, f, indent=4)

    print("转换完成！")


if __name__ == '__main__':
    input_path = r"E:\zhuliang\animal_bird\birds\json/"  # 需要确保文件里只有json文件
    output_path = r"E:\zhuliang\animal_bird\birds\det_json/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    json_dir = pathlib.Path(input_path).expanduser().resolve()
    for cnt, file_name in enumerate(json_dir.iterdir()):  # 先将json文件进行解码
        if file_name.suffix in ['.json']:
            input_json_path = input_path + "/" + file_name.name
            output_json_path = output_path + "/" + file_name.name

            # 使用示例
            convert_semantic_to_detection(input_json_path, output_json_path)
