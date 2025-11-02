# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/18 20:41

'''
读取和分析图像
'''
import os.path
from collections import defaultdict
from pathlib import Path
from PIL import Image

train_size_dict = defaultdict(int)
train_path = Path("D:/mydata/stervel/original_data/train_images/")
for img_name in train_path.iterdir():
    img = Image.open(img_name)
    train_size_dict[img.size] += 1

print(train_size_dict)  # defaultdict(<class 'int'>, {(1600, 256): 12568})

# 读取测试集图像数据
test_size_dict = defaultdict(int)
test_path = Path("D:/mydata/stervel/original_data/test_images")

for img_name in test_path.iterdir():
    img = Image.open(img_name)
    test_size_dict[img.size] += 1

print(test_size_dict)  # defaultdict(<class 'int'>, {(1600, 256): 1801})

'''可视化数据集'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import cv2

train_df = pd.read_csv("D:/mydata/stervel/original_data/train.csv")
# 为了方便可视化，我们为不同的缺陷类别设置颜色显示
palet = [(249, 192, 12), (0, 185, 241), (114, 0, 218), (249, 50, 12)]
fig, ax = plt.subplots(1, 4, figsize=(15, 5))
for i in range(4):
    ax[i].axis('off')
    ax[i].imshow(np.ones((50, 50, 3), dtype=np.uint8) * palet[i])
    ax[i].set_title("class color: {}".format(i + 1))

fig.suptitle("each class colors")
# plt.show()

'''
将不同的缺陷标识归类
'''
idx_no_defect = []
idx_class_1 = []
idx_class_2 = []
idx_class_3 = []
idx_class_4 = []
idx_class_multi = []
idx_class_triple = []

for col in range(0, len(train_df), 4):
    img_names = [str(i).split("_")[0] for i in train_df.iloc[col:col + 4, 0].values]
    if not (img_names[0] == img_names[1] == img_names[2] == img_names[3]):
        raise ValueError

    labels = train_df.iloc[col:col + 4, 1]
    if labels.isna().all():
        idx_no_defect.append(col)
    elif (labels.isna() == [False, True, True, True]).all():
        idx_class_1.append(col)
    elif (labels.isna() == [True, False, True, True]).all():
        idx_class_2.append(col)
    elif (labels.isna() == [True, True, False, True]).all():
        idx_class_3.append(col)
    elif (labels.isna() == [True, True, True, False]).all():
        idx_class_4.append(col)
    elif labels.isna().sum() == 1:
        idx_class_triple.append(col)
    else:
        idx_class_multi.append(col)

train_path = Path("D:/mydata/stervel/original_data/train_images")
'''
创建可视化标注函数
'''


def name_and_mask(start_idx):
    col = start_idx
    img_names = [str(i).split("_")[0] for i in train_df.iloc[col:col + 4, 0].values]
    if not (img_names[0] == img_names[1] == img_names[2] == img_names[3]):
        raise ValueError

    labels = train_df.iloc[col:col + 4, 1]
    mask = np.zeros((256, 1600, 4), dtype=np.uint8)

    for idx, label in enumerate(labels.values):
        if label is not np.nan:
            mask_label = np.zeros(1600 * 256, dtype=np.uint8)
            label = label.split(" ")
            positions = map(int, label[0::2])
            length = map(int, label[1::2])
            for pos, le in zip(positions, length):
                mask_label[pos - 1:pos + le - 1] = 1
            mask[:, :, idx] = mask_label.reshape(256, 1600, order='F')  # 按列取值reshape

    return img_names[0], mask


def show_mask_image_and_save(col, save_path):
    name, mask = name_and_mask(col)
    img = cv2.imread(str(train_path / name))
    fig, ax = plt.subplots(figsize=(15, 15))
    for ch in range(4):
        contours, _ = cv2.findContours(mask[:, :, ch], cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for i in range(0, len(contours)):
            cv2.polylines(img, contours[i], True, palet[ch], 2)

    ax.set_title(name)
    ax.imshow(img)
    cv2.imwrite(save_path + '%s' % (name), img)
    # plt.show()


'''
# 展示5张无缺陷图像
for idx in idx_no_defect[:1]:
    show_mask_image_and_save(idx)
'''

'''
展示5张第一类的图像
for idx in idx_class_1:
    show_mask_image_and_save(idx,save_path='D:/mydata/stervel/severstal-steel-defect-detection/class_1/')
'''

'''展示5张第二类的图像
for idx in idx_class_2:
    show_mask_image_and_save(idx,save_path='D:/mydata/stervel/severstal-steel-defect-detection/class_2/')
'''

'''展示5张第三类的图像
for idx in idx_class_3:
    show_mask_image_and_save(idx,save_path='D:/mydata/stervel/severstal-steel-defect-detection/class_3/')
'''

'''展示5张第四类的图像 
for idx in idx_class_4:
    show_mask_image_and_save(idx,save_path='D:/mydata/stervel/severstal-steel-defect-detection/class_4/')
'''
'''展示多个类别的图像
for idx in idx_class_multi:
    show_mask_image_and_save(idx,save_path='D:/mydata/stervel/severstal-steel-defect-detection/class_multi/')
   '''

import shutil

new_dir = 'D:/mydata/stervel/original_data/no_class_images/no_images'
for i in idx_no_defect:
    name, mask = name_and_mask(i)
    full_path = str("D:/mydata/stervel/original_data/train_images/" + name)
    print(full_path)
    if os.path.isfile(full_path):
        shutil.copy(full_path, new_dir)
