# -*- coding: utf-8 -*-

import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('../opencv_logo.png')

# 2D卷积
kernel = np.ones((5,5), np.float32)/25

# cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
# ddepth –desired depth of the destination image;
# if it is negative, it will be the same as src.depth();
# the following combinations of src.depth() and ddepth are supported: #src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
# src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
# src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
# src.depth() = CV_64F, ddepth = -1/CV_64F
# when ddepth=-1, the output image will have the same depth as the source.

dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


# 平均
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# 高斯模糊
# 0 是指根据窗口大小(5,5)来计算高斯函数标准差 
blur = cv2.GaussianBlur(img,(5,5),0)

# 中值模糊
median = cv2.medianBlur(img,5)

# 双边滤波
# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# d – Diameter of each pixel neighborhood that is used during filtering. # If it is non-positive, it is computed from sigmaSpace
# 9 邻域直径,两个 75 分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)







