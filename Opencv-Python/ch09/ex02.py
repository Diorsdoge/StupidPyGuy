# -*- coding: utf-8 -*-

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

# OpenCV颜色是按照BGR排列，matplotlib的颜色是按照RGB排列

BLUE = [255, 0, 0]

img1 = cv2.imread('../test0.png')

# 重复最后一个元素
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
# 边界元素的镜像 
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT) 
# 跟上面一样，稍微改动
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101) 
# 
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# 添加有颜色的常数值边界    value 是边界颜色
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231), plt.imshow(img1,'gray'), plt.title('ORIGINAL') 
plt.subplot(232), plt.imshow(replicate,'gray'), plt.title('REPLICATE') 
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('REFLECT') 
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101') 
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('WRAP') 
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('CONSTANT')

plt.show()