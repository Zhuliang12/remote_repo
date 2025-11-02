# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/10/8 22:24

import glob

# 存放图片的地址
train_image_path = r"D:\mydata\ori_data\train_images\400x256_all\images/1600x256/"
# valid_image_path = r"D:\mydata\ori_data\train_images\400x256_all\images/valid/"
# test_image_path = r'D:\mydata\ori_data\train_images\400x256_all\images/test/'
# 生成的txt的路径
txt_path = r"D:\mydata\ori_data\train_images\400x256_all\images/"


def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.jpg'):
            tf.write(jpg_file + '\n')


generate_train_and_val(train_image_path, txt_path + '1600x256.txt')
# generate_train_and_val(valid_image_path, txt_path + 'valid.txt')
# generate_train_and_val(test_image_path, txt_path + 'test.txt')
