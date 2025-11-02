# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/3 19:59

'''
对图像进行数据增强，将burying_slag增强到2000张
'''

# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import time
from PIL import Image, ImageChops, ImageEnhance


def image_LR(img, savefilepath, save_filename):
    """ 左右翻转"""
    lr = img.transpose(Image.FLIP_LEFT_RIGHT)  # 左右翻转
    lr.save(savefilepath + save_filename)


def image_TB(img, savefilepath, save_filename):
    """ 上下翻转"""
    ud = img.transpose(Image.FLIP_TOP_BOTTOM)  # 上下翻转
    ud.save(savefilepath + save_filename)


def image_rot_180(img, savefilepath, save_filename):
    """图像旋转20度"""
    out = img.rotate(180)  # 旋转20度
    out.save(savefilepath + save_filename)


def rotate_bound(image, angle, savefilepath, save_filename):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    save_image = cv2.warpAffine(image, M, (nW, nH))
    return cv2.imwrite(savefilepath + save_filename, save_image)


def image_translation_x(img, savefilepath, save_filename):
    """图像x轴平移"""
    out = ImageChops.offset(img, 30, 0)  # 只沿X轴平移
    out.save(savefilepath + save_filename)


def image_translation_y(img, savefilepath, save_filename):
    """图像y轴平移"""
    out = ImageChops.offset(img, 0, 30)  # 只沿y轴平移
    out.save(savefilepath + save_filename)


def image_brightness_weak(img, savefilepath, save_filename):
    """亮度调整"""
    bri = ImageEnhance.Brightness(img)
    bri_img = bri.enhance(0.8)  # 小于1为减弱
    bri_img.save(savefilepath + save_filename)


def image_brightness_enhance(img, savefilepath, save_filename):
    """亮度调整"""
    bri = ImageEnhance.Brightness(img)
    bri_img = bri.enhance(1.2)  # 大于1为增强
    bri_img.save(savefilepath + save_filename)


def image_chroma_weak(img, savefilepath, save_filename):
    """色度调整 减弱"""
    col = ImageEnhance.Color(img)
    col_img = col.enhance(0.8)  # 色度减弱
    col_img.save(savefilepath + save_filename)


def image_chroma_enhance(img, savefilepath, save_filename):
    """色度调整 增强"""
    col = ImageEnhance.Color(img)
    col_img = col.enhance(1.8)  # 色度增强
    col_img.save(savefilepath + save_filename)


def image_contrast_weak(img, savefilepath, save_filename):
    """对比度调整 减弱"""
    con = ImageEnhance.Contrast(img)
    con_img = con.enhance(0.8)  # 对比度减弱
    con_img.save(savefilepath + save_filename)


def image_contrast_enhance(img, savefilepath, save_filename):
    """对比度调整 增强"""
    con = ImageEnhance.Contrast(img)
    con_img = con.enhance(1.8)  # 对比度增强
    con_img.save(savefilepath + save_filename)


def image_sharpness_weak(img, savefilepath, save_filename):
    """锐度调整 减弱"""
    sha = ImageEnhance.Sharpness(img)
    sha_img = sha.enhance(0.8)  # 锐度减弱
    sha_img.save(savefilepath + save_filename)


def image_sharpness_enhance(img, savefilepath, save_filename):
    """锐度调整 增强"""
    sha = ImageEnhance.Sharpness(img)
    sha_img = sha.enhance(1.8)  # 锐度增强
    sha_img.save(savefilepath + save_filename)


# 定义扩充图片函数
def image_expansion(filepath, savefilepath):
    """
    :param filepath: 图片路径
    :param savefilepath: 扩充保存图片路径
    :param save_prefix: 图片前缀
    :return: 图片扩充数据集
    """

    for parent, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            i = int(filename[6:-6])  # 控制遍历的顺序
            image_path = filepath + filename
            print('正在扩充图片：%s' % filename)
            try:
                # img = Image.open(image_path)  # 不使用90度或者别的角度旋转时使用这中方式打开图片
                # if img.mode == "P":
                #     img = img.convert('RGB')
                img = cv2.imread(image_path)  # 使用旋转等增强时使用这行代码

                # image_LR(img, savefilepath, save_filename=filename[:-4] + '_LR' + '.jpg')
                # image_TB(img, savefilepath, save_filename=filename[:-4] + '_TB' + '.jpg')
                #
                # image_rot_180(img, savefilepath, save_filename=filename[:-4] + '_rot180' + '.jpg')
                rotate_bound(img, 90, savefilepath, save_filename=filename[:-4] + '_rot90' + '.jpg')
                rotate_bound(img, 270, savefilepath, save_filename=filename[:-4] + '_rot270' + '.jpg')
                # image_translation_x(img, savefilepath, save_filename=save_prefix + 'X_trans_' + str(i) + '.jpg')
                # image_translation_y(img, savefilepath, save_filename=save_prefix + 'Y_trans_' + str(i) + '.jpg')

                # image_brightness_weak(img, savefilepath, save_filename=filename[:-4] + '_b_weak' + '.jpg')
                # image_brightness_enhance(img, savefilepath, save_filename=filename[:-4] + '_b_enhance' + '.jpg')

                # image_chroma_weak(img, savefilepath, save_filename=filename[:-4] + '_chr_weak' + '.jpg')
                # image_chroma_enhance(img, savefilepath, save_filename=filename[:-4] + '_chr_enhance' + '.jpg')
                #
                # image_contrast_weak(img, savefilepath, save_filename=filename[:-4] + '_cont_weak' + '.jpg')
                # image_contrast_enhance(img, savefilepath, save_filename=filename[:-4] + '_cont_enhance' + '.jpg')
                #
                # image_sharpness_weak(img, savefilepath, save_filename=filename[:-4] + '_sharp_weak' + '.jpg')
                # image_sharpness_enhance(img, savefilepath, save_filename=filename[:-4] + '_sharp_enhance' + '.jpg')

            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    # 设置图片路径
    filepath = r'C:\Users\liang\Desktop\ori_data\images\400x256_all\multi\striped/'

    # 设置扩充保存图片路径
    savefilepath = r'C:\Users\liang\Desktop\ori_data\images\400x256_all\multi\striped/'

    # 设置前缀图片名称

    time1 = time.time()
    image_expansion(filepath, savefilepath)
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
