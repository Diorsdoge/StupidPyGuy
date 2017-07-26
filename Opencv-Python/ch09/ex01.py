# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../test0.png')

# 根据像素的行列获取像素值，返回为B, G, R
px = img[100, 100]
print px
blue = img[100, 100, 0]
print blue

# 修改像素值
img[100, 100] = [255, 255, 255]
print img[100, 100]

# 修改像素值更好的方法
print img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)
print img.item(10, 10, 2)

## 50
## 100

# 打印行、列、通道
print img.shape

# 打印图像像素数目
print img.size

# 打印图像的数据类型
print img.dtype

# 复制图像某一区域，替换另一区域
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# 拆分和合并通道
b, g, r = cv2.split(img)
img = cv2.merge(b, g, r)














