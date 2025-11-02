# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/5/27 20:51

import os
import cv2
import numpy as np
import random


def sp_noise(noise_img, proportion):
    '''
    proportion的值表示加入噪声的量，可根据需要自行调整
    '''
    height, width = noise_img.shape[0], noise_img.shape[1]  # 获取高度宽度像素值
    num = int(height * width * proportion)  # 一个准备加入多少噪声小点
    for i in range(num):
        w = random.randint(0, width - 1)
        h = random.randint(0, height - 1)
        if random.randint(0, 1) == 0:
            noise_img[h, w] = 0
        else:
            noise_img[h, w] = 255
    return noise_img


def convert(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for filename in os.listdir(input_dir):
        path = input_dir + "/" + filename  # 获取文件路径
        print("doing... ", path)
        noise_img = cv2.imread(path)  # 读取图片
        img_noise = sp_noise(noise_img, 0.025)
        new_filename = filename.split('.')[0] + '_SP.jpg'
        cv2.imwrite(output_dir + '/' + new_filename, img_noise)


if __name__ == '__main__':
    input_dir = r"E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\train/"  # 输入数据文件夹
    output_dir = r"E:\work\zhuanzhuzhilian\KMSN_Optical_flow_method\Dataset_create\noise/"  # 输出数据文件夹
    convert(input_dir, output_dir)
    print('finish')
