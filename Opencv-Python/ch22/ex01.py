# -*- coding: utf-8 -*-

import numpy as np 
import cv2
from matplotlib import pyplot as plt

# 统计一幅图的直方图
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# images: 原图像（图像格式为 uint8 或 float32 ）。当传入函数时应用中括号 [] 括 来 例如 [img]。
# channels: 同样  用中括号括 来 它会告 函数我们 统  幅图 像的直方图。如果 入图像是灰度图 它的值就是 [0] 如果是彩色图像 的  传入的参数可以是 [0] [1] [2] 它们分别对应着   B G R。
# mask: 掩模图像。 统 整幅图像的直方图就把它设为None。但是如果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像，并使用它。 后 有例子 
# histSize: BIN 的数目。也应该用中括号括起来，例如：[256]。
# ranges: 像素值范围通常为 [0 256]


# 绘制直方图
img = cv2.imread('home.jpg', 0)
plt.hist(img.ravel(), 256, [0,256])
plt.show()

# 同时绘制多通道
img = cv2.imread('home.jpg')
color = ('b','g','r')
# 对一个列 或数组既  历索引又  历元素时
# 使用内置 enumerrate 函数会有更加直接 优美的做法 
# enumerate 会将数组或列 组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

# 使用掩模
img = cv2.imread('home.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256]) 
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()

# 直方图均衡化
img = cv2.imread('wiki.jpg',0)
# flatten() 将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

img = cv2.imread('wiki.jpg',0) 
equ = cv2.equalizeHist(img) 
res = np.hstack((img,equ))
#stacking images side-by-side 
cv2.imwrite('res.png',res)

# create a CLAHE object (Arguments are optional).
# 不知 为什么我没好到 createCLAHE  个模块
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)




