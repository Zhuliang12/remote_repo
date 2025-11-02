# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/4 14:15

import os
import numpy as np
import time

txt_filename = 'D:/mydata/stervel/original_data/class_2_images/2_txt/'
txt_aug_path = 'D:/mydata/stervel/original_data/class_2_images/aug_labels/'


def labels_ORI(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_strxy = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_LR(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_x = '%.6f' % float(1 - x)
            new_strxy = str(new_x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_TB(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_y = '%.6f' % float(1 - y)
            new_strxy = str(x) + ' ' + str(new_y) + ' ' + str(w) + ' ' + str(h)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_rot_180(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_x = '%.6f' % float(1 - x)
            new_y = '%.6f' % float(1 - y)
            new_strxy = str(new_x) + ' ' + str(new_y) + ' ' + str(w) + ' ' + str(h)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_rot_270(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_x = '%.6f' % float(1 - x)
            new_strxy = str(y) + ' ' + str(new_x) + ' ' + str(h) + ' ' + str(w)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_rot_90(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_x = '%.6f' % float(1 - y)
            new_strxy = str(new_x) + ' ' + str(x) + ' ' + str(h) + ' ' + str(w)
            new_strxy = label + ' ' + new_strxy
            faug.writelines(new_strxy + '\n')


def labels_translation_x(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_x = '%.6f' % float(x + 0.01875)
            border_x_R = float(new_x) + float(w / 2)
            border_X_L = float(new_x) - float(w / 2)
            if border_x_R <= 1.0:
                new_strxy = str(new_x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
                new_strxy = label + ' ' + new_strxy
                faug.writelines(new_strxy + '\n')
            elif border_X_L > 1.0:
                new_x = '%.6f' % (float(new_x) - float(1.0))
                new_strxy = str(new_x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
                new_strxy = label + ' ' + new_strxy
                faug.writelines(new_strxy + '\n')
            elif border_X_L < 1.0 and border_x_R > 1.0:
                new_w1 = '%.6f' % float(1.0 - border_X_L)
                new_w2 = '%.6f' % float(border_x_R - 1.0)
                new_x1 = '%.6f' % float(float(1.0) - (float(new_w1) / 2))
                new_x2 = '%.6f' % (float(new_w2) / 2)
                new_strxy1 = str(new_x1) + ' ' + str(y) + ' ' + str(new_w1) + ' ' + str(h)
                new_strxy1 = label + ' ' + new_strxy1
                faug.writelines(new_strxy1 + '\n')
                new_strxy2 = str(new_x2) + ' ' + str(y) + ' ' + str(new_w2) + ' ' + str(h)
                new_strxy2 = label + ' ' + new_strxy2
                faug.writelines(new_strxy2 + '\n')


def labels_translation_y(label, save_path, save_name):
    txt_path = save_path + save_name
    with open(txt_path, 'w+') as faug:
        f = open(label, "r",
                 encoding='utf-8',
                 errors='ignore')
        for line in f:
            label = line.split(' ')[0]
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            w = float(line.split(' ')[3])
            h = float(line.split(' ')[4])
            new_y = '%.6f' % float(y + 0.1172)
            border_y_T = float(new_y) + float(h / 2)
            border_y_B = float(new_y) - float(h / 2)
            if border_y_T <= 1.0:
                new_strxy = str(x) + ' ' + str(new_y) + ' ' + str(w) + ' ' + str(h)
                new_strxy = label + ' ' + new_strxy
                faug.writelines(new_strxy + '\n')
            elif border_y_B > 1.0:
                new_y = float(new_y) - float(1.0)
                new_strxy = str(x) + ' ' + str(new_y) + ' ' + str(w) + ' ' + str(h)
                new_strxy = label + ' ' + new_strxy
                faug.writelines(new_strxy + '\n')
            elif border_y_B < 1.0 and border_y_T > 1.0:
                new_h1 = '%.6f' % float(1.0 - border_y_B)
                new_h2 = '%.6f' % float(border_y_T - 1.0)
                new_y1 = '%.6f' % (float(1.0) - float(new_h1) / 2)
                new_y2 = '%.6f' % (float(new_h2) / 2)
                new_strxy1 = str(x) + ' ' + str(new_y1) + ' ' + str(w) + ' ' + str(new_h1)
                new_strxy1 = label + ' ' + new_strxy1
                faug.writelines(new_strxy1 + '\n')
                new_strxy2 = str(x) + ' ' + str(new_y2) + ' ' + str(w) + ' ' + str(new_h2)
                new_strxy2 = label + ' ' + new_strxy2
                faug.writelines(new_strxy2 + '\n')


def enhance_labels(txt_path, save_path):
    for parent, dirnames, filenames in os.walk(txt_path):
        for filename in filenames:
            i = int(filename[6:-6])
            label_path = txt_path + filename
            print('正在扩充标签：%s' % filename)
            try:
                # print('LR')
                # labels_LR(label_path, save_path, save_name=filename[:-4] + '_LR' + '.txt')
                # print('TB')
                # labels_TB(label_path, save_path, save_name=filename[:-4] + '_TB' + '.txt')
                # print('rot180')
                # labels_rot_180(label_path, save_path, save_name=filename[:-4] + '_rot180' + '.txt')
                labels_rot_90(label_path, save_path, save_name=filename[:-4] + '_rot90' + '.txt')
                labels_rot_270(label_path, save_path, save_name=filename[:-4] + '_rot270' + '.txt')
                # print('X_trans')
                # labels_translation_x(label_path, save_path, save_name=save_prefix + 'X_trans_' + str(i) + '.txt')
                # print('Y_trans')
                # labels_translation_y(label_path, save_path, save_name=save_prefix + 'Y_trans_' + str(i) + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_b_weak' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_b_enhance' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_chr_weak' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_chr_enhance' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_cont_weak' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_cont_enhance' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_sharp_weak' + '.txt')
                # labels_ORI(label_path, save_path, save_name=filename[:-4] + '_sharp_enhance' + '.txt')
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    txt_path = r'C:\Users\liang\Desktop\ori_data\images\400x256_all\labels\1/'
    save_path = r'C:\Users\liang\Desktop\ori_data\images\400x256_all\labels\1/'

    time1 = time.time()
    enhance_labels(txt_path, save_path)
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
