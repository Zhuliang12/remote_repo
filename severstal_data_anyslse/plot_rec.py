# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/26 18:59
'''
绘图
'''
import cv2 as cv
import os

img = cv.imread('new_BGR.jpg')
print(img.shape)

rec_image = cv.rectangle(img, (0, int(12.75)), (8, int(23.75)), (0, 255, 0), int(1.5))
rec1_image = cv.rectangle(rec_image, (8 + 5, int(12.75)), (26 + 5, int(32.75)), (255, 0, 0), int(1.5))
rec2_image = cv.rectangle(rec1_image, (26 + 10, int(12.75)), (36 + 10, int(54.75)), (0, 0, 255), int(1.5))
rec3_image = cv.rectangle(rec2_image, (36 + 15, int(12.75)), (44 + 15, int(110.75)), (255, 255, 0), int(1.5))
rec4_image = cv.rectangle(rec3_image, (44 + 20, int(12.75)), (60 + 20, int(109.75)), (255, 0, 255), int(1.5))
rec5_image = cv.rectangle(rec4_image, (60 + 25, int(12.75)), (118 + 25, int(41.75)), (0, 255, 255), int(1.5))
rec6_image = cv.rectangle(rec5_image, (118 + 30, int(12.75)), (159 + 30, int(111.75)), (100, 0, 0), int(1.5))
rec7_image = cv.rectangle(rec6_image, (159 + 35, int(12.75)), (269 + 35, int(84.75)), (0, 100, 0), int(1.5))
rec8_image = cv.rectangle(rec7_image, (269 + 40, int(12.75)), (571 + 40, int(52.75)), (0, 0, 100), int(1.5))
cv.imshow('rec', rec8_image)
cv.waitKey(0)
cv.imwrite('Kmeans++.png', rec8_image)
