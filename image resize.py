# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/6 21:51

import cv2
import numpy as np


# 使用PIL库读入图片并进行resize

def preprocess(img, input_shape, letter_box=True):  # 是将图片变成我们要的样子 将图片边成1600，1600
    # 这种方法对于长宽比差距很大的图片是很大的考验，会丢失很多的像素信息
    '''
    img: 输入的图片
    input_shape: 输入图片的大小
    letter_box: 信箱
    '''
    if letter_box:
        img_h, img_w, _ = img.shape  # 256  1600
        new_h, new_w = input_shape[0], input_shape[1]  # 400，400
        offset_h, offset_w = 0, 0  # 高补偿 宽补偿
        if (new_w / img_w) <= (new_h / img_h):  # new_w/img_w=1/4 new_h/img_h=400/256
            new_h = int(img_h * new_w / img_w)  # new_h=256*400/1600=64
            offset_h = (input_shape[0] - new_h) // 2  # 高补偿 (400-64)/2=168
        else:
            new_w = int(img_w * new_h / img_h)
            offset_w = (input_shape[1] - new_w) // 2
        resized = cv2.resize(img, (new_w, new_h))
        img = np.full((input_shape[0], input_shape[1], 3), 127, dtype=np.uint8)  # 生成一个全是127的数组
        img[offset_h:(offset_h + new_h), offset_w:(offset_w + new_w), :] = resized  # 将resized的数据加载到这里
    else:
        img = cv2.resize(img, (input_shape[1], input_shape[0]))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将输入的图片色彩区域改成RGB空间
    # img = img.transpose((2, 0, 1)).astype(np.float32)  # 变成 3 height width
    # img /= 255.0  # 进行归一化
    return img


img_path = 'D:/mydata/test/test1/images/'
import os

images = os.listdir(img_path)
#print(images)
for i in images:
    path=img_path+str(i)
    img = cv2.imread(path)
    new_img=preprocess(img,(1600,1600))
    cv2.imwrite(str(i),new_img)

