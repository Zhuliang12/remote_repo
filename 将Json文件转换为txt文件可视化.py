# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/6/7 18:14

def check_convert_json_label_to_yolov_seg_label():
    """
    验证一下对不对
    :return:
    """
    import glob
    import numpy as np
    import cv2
    txt_path = r"C:/Users/liang/Desktop/myyolo/yolov5-seg-master/dataset/labels/vision/";
    txt_files = glob.glob(txt_path + "/*.txt")
    for txt_file in txt_files:
        # if json_file != r"C:\Users\jianming_ge\Desktop\code\handle_dataset\water_street\223.json":
        # continue
        print(txt_file)
        pic_path = txt_file.replace(".txt", ".jpg")
        img = cv2.imread(pic_path)
        height, width, _ = img.shape
        print(height, width)

        # cv2.imshow("111",img)
        # 显示原始图片
        # cv2.waitKey()
        # 勾勒多边形
        file_handle = open(txt_file)
        cnt_info = file_handle.readlines()
        new_cnt_info = [line_str.replace("\n", "").split(" ") for line_str in cnt_info]
        print(len(new_cnt_info))
        print("---====---")
        # 45 bowl 碗 49 橘子 50 西兰花
        color_map = {"0": (0, 255, 255), "1": (255, 0, 255), "2": (255, 255, 0), "3": (110, 255, 0)}
        for new_info in new_cnt_info:
            print(new_info)
            s = []
            for i in range(1, len(new_info), 2):
                b = [float(tmp) for tmp in new_info[i:i + 2]]
                s.append([int(b[0] * width), int(b[1] * height)])
            print(s)
            cv2.polylines(img, [np.array(s, np.int32)], True, color_map.get(new_info[0]))
        cv2.imshow('img2', img)
        cv2.waitKey()


check_convert_json_label_to_yolov_seg_label()
