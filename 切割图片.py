#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/7/3 13:14

import os
from PIL import Image

file_path = r'D:\mydata\stervel\seversatl_data\test/'
save_path = r'C:\Users\liang\Desktop\ori_data\images\400x256_test/'
if not os.path.exists(save_path):
    os.mkdir(save_path)
file_name = os.listdir(file_path)
# print(file_name)
for name in file_name:
    path = file_path + name
    print(path)
    img = Image.open(path)
    name_without_suffix = name[:-4]
    # 打开一张图片

    # 图片尺寸
    img_size = img.size

    h = int(img_size[1])  # 图片高度
    w = int(img_size[0])  # 图片宽度
    # 将图片分成三部分，这部分可以自己更改
    for i in range(1, 5):
        if i == 1:
            region = img.crop((int(0), 0, int(w / 4), h))  # crop函数里面四个数据分别为左、上、右、下，按照这个规则来分割你想的比例图片。
            region.save(save_path + '/' + f"{name_without_suffix}_1.jpg")
        else:
            if i == 2:
                region = img.crop((int(w / 4), 0, int(w * 2 / 4), h))
                region.save(save_path + '/' + f"{name_without_suffix}_2.jpg")
            else:
                if i == 3:
                    region = img.crop((int(w * 2 / 4), 0, int(w * 3 / 4), h))
                    region.save(save_path + '/' + f"{name_without_suffix}_3.jpg")
                else:
                    region = img.crop((int(w * 3 / 4), 0, w, h))
                    region.save(save_path + '/' + f"{name_without_suffix}_4.jpg")

        print("处理结束！")
