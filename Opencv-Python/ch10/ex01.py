# -*- coding: utf-8 -*-

import cv2
import numpy as np 

x = np.uint8([250])
y = np.uint8([10])
print cv2.add(x, y) # 250＋10 ＝ 260 => 255
[[255]]
print x+y       # 250+10 = 260 % 256 = 4
[4]

# 图像混合
img1 = cv2.imread('test0.png')
img2 = cv2.imread('opencv_logo.jpg')

# dst = alpha*img1 + beta*img2 + gama
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()