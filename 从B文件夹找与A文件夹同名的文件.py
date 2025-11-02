# ==========================================================
# 模块名  ：从B文件夹中抽取与A文件夹同名的文件
# 文件名  ：从B文件找与A文件夹同名的文件.py
# 相关文件：无
# 作者    ：Liangliang Bai (liangliang.bai@leapting.com)
# 版权    ：<Copyright(C) 2022- Hu Zhou leapting Technology Co., Ltd. All rights reserved.>
# 修改记录：
# 日  期        版本     修改人   走读人  修改记录
#
# 2023.07.18    1.0.0.1  白亮亮
# ==========================================================


import os
import cv2


# 函数功能：获取指定文件夹下的所有文件名
# ------>parameters<------ #
# inputParas:
#     org_image_dir:文件夹路径；
#     org_image_dir:文件夹路径；
# outputParas:
#     image_name_list：文件名列表；
# ------>parameters<------ #
def get_image_name_list(org_image_dir: str) -> list:
    dst_image_name_list = os.listdir(org_image_dir)
    return dst_image_name_list


# 函数功能：获取org_image_dir文件夹下的所有文件名，再从new_image_dir文件夹挑出来并存放到dst_image_dir文件夹下；
# ------>parameters<------ #
# inputParas:
#     org_image_dir:原文件夹路径；
#     new_image_dir:新文件夹路径；
#     dst_image_dir:目标文件夹路径
# outputParas:
#     image_name_list：文件名列表；
# ------>parameters<------ #
def get_target_image(org_image_dir: str, new_image_dir: str, dst_image_dir: str):
    if not os.path.exists(org_image_dir):
        raise Exception("路径不存在，请检查！")
    if not os.path.exists(new_image_dir):
        raise Exception("路径不存在，请检查！")
    if not os.path.exists(dst_image_dir):
        os.mkdir(dst_image_dir)
    dst_image_name_list = get_image_name_list(org_image_dir)

    for image_name in dst_image_name_list:
        image_path = os.path.join(new_image_dir, image_name)
        dst_image_path = os.path.join(dst_image_dir, image_name)
        image = cv2.imread(image_path)
        cv2.imwrite(dst_image_path, image)


if __name__ == '__main__':
    org_image_dir = "D:/code_written_in_mega/ultralytics-main/ultralytics/yolo/v8/detect/runs/detect/xxx/"
    new_image_dir = "D:/LT_DATASETS_PATROL_ROBOT/20230718-huzhouData/orgImg/"
    dst_image_dir = "D:/LT_DATASETS_PATROL_ROBOT/20230718-huzhouData/dstImage/"
    get_target_image(org_image_dir, new_image_dir, dst_image_dir)