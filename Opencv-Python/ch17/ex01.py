# -*- coding: utf-8 -*-

import cv2
import numpy as np


img = cv2.imread('../test0.png',0)
img1 = cv2.imread('../test0.png',0)
# 腐蚀
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

# 膨胀
dilation = cv2.dilate(img,kernel,iterations = 1)

# 开运算——先腐蚀，再膨胀，去除噪声
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)

# 闭运算——先膨胀，再腐蚀，去除前景小黑点
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 形态学梯度——膨胀和腐蚀的差，看上去像前景物体轮廓
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 礼帽——原始图像与进行开运算得到的图像的额差。
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽——进行闭运算之后得到的图像与原始图像的差。
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)




cv2.imshow('iamge', img)
cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

