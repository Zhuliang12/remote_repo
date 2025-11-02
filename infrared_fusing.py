#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/8/2 13:18

import pywt
import cv2
import numpy as np
import threading


class ImgFusion:
    def TIF_algo(self, p1, p2, median_blur_value=3, mean_blur_value=35):
        p1_b = cv2.blur(p1, (mean_blur_value, mean_blur_value))
        p1_b = p1_b.astype(np.float)
        p2_b = cv2.blur(p2, (mean_blur_value, mean_blur_value))
        p2_b = p2_b.astype(np.float)
        # cv2.imshow('picture after mean blur p1_b', p1_b)
        # cv2.imshow('picture after mean blur p2_b', p2_b)

        # p1_d = abs(p1.astype(np.float) - p1_b)
        # p2_d = abs(p2.astype(np.float) - p2_b)
        p1_d = p1.astype(np.float) - p1_b
        p2_d = p2.astype(np.float) - p2_b
        # cv2.imshow('detail layer p1', p1_d / 255.0)
        # cv2.imshow('detail layer p2', p2_d / 255.0)

        p1_after_medianblur = cv2.medianBlur(p1, median_blur_value)
        p2_after_medianblur = cv2.medianBlur(p2, median_blur_value)
        # cv2.imshow('picture after median blur p1_after_medianblur', p1_after_medianblur)
        # cv2.imshow('picture after median blur p2_after_medianblur', p2_after_medianblur)

        p1_after_medianblur = p1_after_medianblur.astype(np.float)
        p2_after_medianblur = p2_after_medianblur.astype(np.float)

        p1_subtract_from_median_mean = p1_after_medianblur - p1_b + 0.0001
        p2_subtract_from_median_mean = p2_after_medianblur - p2_b + 0.0001
        # cv2.imshow('subtract_from_median_mean  p1_subtract_from_median_mean', p1_subtract_from_median_mean/255.0)
        # cv2.imshow('subtract_from_median_mean  p2_subtract_from_median_mean', p2_subtract_from_median_mean/255.0)
        m1 = p1_subtract_from_median_mean[:, :, 0]
        m2 = p1_subtract_from_median_mean[:, :, 1]
        m3 = p1_subtract_from_median_mean[:, :, 2]
        res = m1 * m1 + m2 * m2 + m3 * m3
        # delta1 = np.sqrt(res)
        delta1 = res
        m1 = p2_subtract_from_median_mean[:, :, 0]
        m2 = p2_subtract_from_median_mean[:, :, 1]
        m3 = p2_subtract_from_median_mean[:, :, 2]
        res = m1 * m1 + m2 * m2 + m3 * m3

        delta2 = abs(m1)

        delta_total = delta1 + delta2

        psi_1 = delta1 / delta_total
        psi_2 = delta2 / delta_total
        psi1 = np.zeros(p1.shape, dtype=np.float)
        psi2 = np.zeros(p2.shape, dtype=np.float)
        psi1[:, :, 0] = psi_1
        psi1[:, :, 1] = psi_1
        psi1[:, :, 2] = psi_1
        psi2[:, :, 0] = psi_2
        psi2[:, :, 1] = psi_2
        psi2[:, :, 2] = psi_2

        p_b = 0.5 * (p1_b + p2_b)
        # cv2.imshow('base pic1', p1_b / 255.0)
        # cv2.imshow('base pic2', p2_b / 255.0)
        # cv2.imshow('base pic', p_b / 255.0)

        p_d = psi1 * p1_d + psi2 * p2_d
        # cv2.imshow('detail layer plus', p_d / 255.0)
        # cv2.imshow('detail pic plus psi1 psi1 * p1_d', psi1 * p1_d)
        # cv2.imshow('detail pic plus psi1 psi2 * p2_d', psi2 * p2_d)
        p = p_b + p_d
        # img = cv2.cvtColor(p, cv2.COLOR_BGR2RGB)
        # cv2.imshow('final result', p / 255.0)
        # cv2.imwrite('./final_res.jpg', p)
        # cv2.waitKey(0)

        return p

    def strategy(self, arr_hvd1, arr_hvd2):
        k1 = 0.8
        k2 = 0.2
        arr_w1 = np.where(np.abs(arr_hvd1) > np.abs(arr_hvd2), k1, k2)
        arr_w2 = np.where(np.abs(arr_hvd1) < np.abs(arr_hvd2), k1, k2)
        return arr_w1, arr_w2

    def fusion(self, arr_visible, arr_infrared):
        it_h1 = arr_visible.shape[0]
        it_w1 = arr_visible.shape[1]
        it_h2 = arr_infrared.shape[0]
        it_w2 = arr_infrared.shape[1]
        if it_h1 % 2 != 0:
            it_h1 = it_h1 + 1
        if it_w1 % 2 != 0:
            it_w1 = it_w1 + 1
        if it_h2 % 2 != 0:
            it_h2 = it_h2 + 1
        if it_w2 % 2 != 0:
            it_w2 = it_w2 + 1
        arr_visible = cv2.resize(arr_visible, (it_w1, it_h1))
        arr_infrared = cv2.resize(arr_infrared, (it_w2, it_h2))

        it_level = 5

        arr_Gray1, arr_Gray2 = cv2.cvtColor(arr_visible, cv2.COLOR_BGR2GRAY), cv2.cvtColor(arr_infrared,
                                                                                           cv2.COLOR_BGR2GRAY)

        arr_Gray1 = arr_Gray1 * 1.0
        arr_Gray2 = arr_Gray2 * 1.0

        arr_visible = arr_visible * 1.0
        arr_infrared = arr_infrared * 1.0

        arr_decGray1 = pywt.wavedec2(arr_Gray1, 'sym4', level=it_level)
        arr_decGray2 = pywt.wavedec2(arr_Gray2, 'sym4', level=it_level)

        ls_decRed1 = pywt.wavedec2(arr_visible[:, :, 0], 'sym4', level=it_level)
        ls_decGreen1 = pywt.wavedec2(arr_visible[:, :, 1], 'sym4', level=it_level)
        ls_decBlue1 = pywt.wavedec2(arr_visible[:, :, 2], 'sym4', level=it_level)
        ls_recRed = []
        ls_recGreen = []
        ls_recBlue = []

        for it_i, (arr_gray1, arr_gray2, arr_red1, arr_green1, arr_blue1) in enumerate(
                zip(arr_decGray1, arr_decGray2, ls_decRed1, ls_decGreen1, ls_decBlue1)):
            if it_i == 0:
                fl_w1 = 0.5
                fl_w2 = 0.5
                us_recRed = fl_w1 * arr_red1 + fl_w2 * arr_gray2
                us_recGreen = fl_w1 * arr_green1 + fl_w2 * arr_gray2
                us_recBlue = fl_w1 * arr_blue1 + fl_w2 * arr_gray2
            else:
                us_recRed = []
                us_recGreen = []
                us_recBlue = []
                for arr_grayHVD1, arr_grayHVD2, arr_redHVD1, arr_greenHVD1, arr_blueHVD1, in zip(arr_gray1, arr_gray2,
                                                                                                 arr_red1, arr_green1,
                                                                                                 arr_blue1):
                    arr_w1, arr_w2 = self.strategy(arr_grayHVD1, arr_grayHVD2)
                    arr_recRed = arr_w1 * arr_redHVD1 + arr_w2 * arr_grayHVD2
                    arr_recGreen = arr_w1 * arr_greenHVD1 + arr_w2 * arr_grayHVD2
                    arr_recBlue = arr_w1 * arr_blueHVD1 + arr_w2 * arr_grayHVD2

                    us_recRed.append(arr_recRed)
                    us_recGreen.append(arr_recGreen)
                    us_recBlue.append(arr_recBlue)

            ls_recRed.append(us_recRed)
            ls_recGreen.append(us_recGreen)
            ls_recBlue.append(us_recBlue)

        arr_rec = np.zeros(arr_visible.shape)
        arr_rec[:, :, 0] = pywt.waverec2(ls_recRed, 'sym4')
        arr_rec[:, :, 1] = pywt.waverec2(ls_recGreen, 'sym4')
        arr_rec[:, :, 2] = pywt.waverec2(ls_recBlue, 'sym4')
        return arr_rec


img_rgb = cv2.imread('new.jpg')
img_t = cv2.imread('new.jpg')
f = ImgFusion()
# five ways of fusion
img_f = f.TIF_algo(img_rgb, img_t)
# img_f = f.fusion(img_rgb,img_t)
# img_f =cv2.addWeighted(img_rgb,0.5, img_t,0.5,0)
# img_f = np.where(img_f > 255.0, 255.0,img_f)
# img_f = np.where(img_f < 0.0, 0.0,img_f)
