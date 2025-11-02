# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/6 15:15
'''
按照后缀移动图片，
move_images_from_different_files 和 copy_images_from_different_files  在新文件夹中存在相同的文件会发生报错
move_images_from_files 和 copy_images_from_files 在文件夹中存在相同文件会先删除相同文件 ，不会发生报错
'''

import os
import shutil


# new_filelist = filesname[start:end]
# print(new_filelist)
def move_images_from_different_files(tagfir, new_dir, tagfile):
    filesname = os.listdir(tagfir)
    for filename in filesname:
        image_path = tagdir + os.sep + filename
        image_list = os.listdir(image_path)
        for name in image_list:
            fulldir = os.path.join(image_path, name)
            print(fulldir)
            if tagfile in os.path.split(fulldir)[1]:
                if os.path.isfile(fulldir):
                    shutil.move(fulldir, new_dir)


def copy_images_from_different_files(tagfir, new_dir, tagfile):
    filesname = os.listdir(tagfir)
    for filename in filesname:
        image_path = tagdir + os.sep + filename
        image_list = os.listdir(image_path)
        for name in image_list:
            fulldir = os.path.join(image_path, name)
            print(fulldir)
            if tagfile in os.path.split(fulldir)[1]:
                if os.path.isfile(fulldir):
                    shutil.copy(fulldir, new_dir)


def copy_images_from_files(tagdir, new_dir, tagfile):
    filesname = os.listdir(tagdir)
    for name in filesname:
        fulldir = os.path.join(tagdir, name)
        # new_file = new_dir + os.sep + name
        # if new_file
        # os.remove(new_file)
        print(fulldir)
        if tagfile in os.path.split(fulldir)[1]:
            if os.path.isfile(fulldir):
                shutil.copy(fulldir, new_dir)


def move_images_from_files(tagdir, new_dir, tagfile):
    filesname = os.listdir(tagdir)
    for name in filesname:
        fulldir = os.path.join(tagdir, name)
        new_file = new_dir + os.sep + name
        if os.path.exists(new_file):
            os.remove(new_file)
        # print(f'{new_file= }')
        print(fulldir)
        if tagfile in os.path.split(fulldir)[1]:
            if os.path.isfile(fulldir):
                shutil.move(fulldir, new_dir)


if __name__ == "__main__":
    tagdir = r'E:\行人识别给朱亮的数据\第二批coco数据/txt/'  # 要处理的目标文件夹
    new_dir = r"E:\zhuliang\person\txt/"  # 要放到的目标文件夹
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)  # 文件夹不存在则创建文件夹
    tagfile = '.txt'  # 想要移动的文件后缀
    copy_images_from_files(tagdir, new_dir, tagfile)
    print('finished')
