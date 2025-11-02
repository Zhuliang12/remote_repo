#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/9/27 12:59
import matplotlib.pyplot as plt
from PIL import Image
import os

image_folder = r'E:\zhuliang\xunjian\tryout\datasets\birds\images\train/'

image_files = {f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')}
width_list = []
height_list = []
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            width_list.append(width)
            height_list.append(height)
            print(f"image:{image_file},width:{width}px,height:{height}px")
    except Exception as e:
        print(f'无法处理图片：{image_file},错误信息：{e}')

print(width_list, '\n', height_list)
plt.scatter(width_list, height_list)
plt.title('images')
plt.xlabel('width')
plt.ylabel('height')
