# -*- coding: utf-8 -*-

import numpy as np 
import cv2
from matplotlib import pyplot as plt


# numpy中的直方图反向投影

# roi is the object or region of object we need to find
roi = cv.imread('rose_red.png')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# target is the image we search in
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# Find the histogram using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
B=cv2.filter2D(B,-1,disc)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)
ret,thresh = cv2.threshold(B,50,255,0)

# opencv中的反向投影

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
# 归一化 原始图像 结果图像 映射到结果图像中的最小值 最大值 归一化类型 
# cv2.NORM_MINMAX 对数组的所有值归一化 使它们线性映射到最小值和最大值之间  
# 归一化之后的直方图便于显示 归一化之后就成了 0 到 255 之 的数了。 
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
# 此处卷积可以把分散的点 在一 
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) 
dst=cv2.filter2D(dst,-1,disc)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
# 别忘了是三  图像 因此  使用 merge 变成 3    
thresh = cv2.merge((thresh,thresh,thresh))

# 按位操作
res = cv2.bitwise_and(target,thresh)
res = np.hstack((target,thresh,res)) 
cv2.imwrite('res.jpg',res)

# 显示图像
cv2.imshow('1',res)
cv2.waitKey(0)


