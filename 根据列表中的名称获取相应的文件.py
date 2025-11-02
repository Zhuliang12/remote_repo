#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/9/14 10:12

import os
import shutil

file_list = [319188, 351428, 274052, 355225, 406275, 407180, 280852, 3389, 62131, 92377, 126869, 62549, 95022, 255684,
             55534, 64016, 97201, 256177, 56562, 65198, 109659, 271622, 58210, 68203, 110259, 272635, 58483, 70295,
             118838, 272852, 58785, 72800, 119891, 273710, 59039, 76107]

goa_path = r'E:\zhuliang\coco-animal\images\train2017/'
new_path = r'E:\zhuliang\coco-animal\images\birds/'
if not os.path.exists(new_path):
    os.makedirs(new_path)

# filesname.sort()
tagfile = '.jpg'
# print(filesname)

for name in file_list:
    # print(name)1
    # print(str(name).split('.')[0][0:7])
    # name = str(name)[:-5] + str(tagfile)
    name = str(name).zfill(12) + str(tagfile)
    # print(name)
    fullpath = os.path.join(goa_path, name)
    if tagfile in os.path.split(fullpath)[1]:
        print(fullpath)
        if os.path.isfile(fullpath):
            shutil.copy(fullpath, new_path)
        else:
            print('未找到：', fullpath)

print('finished!!')
