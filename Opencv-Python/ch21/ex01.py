# -*- coding: utf-8 -*-

import numpy as np 
import cv2

im = cv2.imread('../test0.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.fincContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 绘制独立轮廓，如第四个轮廓
img = cv2.drawContour(img, contours, -1, (0, 255, 0), 3)

# 单大多数的时候，下面的方法更有用
img = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
