#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2024/9/5 8:50

import shutil
import os


def move_folder(src, dst):
    """
    移动文件夹从 src 到 dst。

    参数:
    src: str, 源文件夹路径
    dst: str, 目标文件夹路径
    """
    # 检查源文件夹是否存在
    if not os.path.exists(src):
        raise FileNotFoundError(f"源文件夹 '{src}' 不存在")

    # 检查目标文件夹是否已经存在
    if os.path.exists(dst):
        raise FileExistsError(f"目标文件夹 '{dst}' 已经存在")

    # 移动文件夹
    shutil.copy(src, dst)
    print(f"文件夹 '{src}' 已成功移动到 '{dst}'")


# 使用示例
source_folder = 'E:/SW_model'
destination_folder = 'F:/SW_model'

try:
    move_folder(source_folder, destination_folder)
except Exception as e:
    print(f"发生错误: {e}")
