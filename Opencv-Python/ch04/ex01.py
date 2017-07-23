# -- coding: utf-8 --

import numpy as np 
import cv2
from matplotlib import pyplot as plt # python绘图库

# 读入图像
# Load an color image in grayscale
img = cv2.imread('../test0.png', 0)

# 事先创建一个window，可调整大小
cv2.nameWindow('image', cv2.WINDOW_NORMAL)

# 显示图像
cv2.imshow('image', img)
# cv2.waiKey(0)
k = cv2.waiKey(0)
if k == 27:	# wait for ESC key to exit
	cv2.destroyAllWindows() # 删除所有窗口，删除自定窗口使用cv2.destroyWindow(windowname)
elif k == ord('s') # wait for 's' key to save and exit
	cv2.imwrite('test0Gray.png', img) # 保存图像
	cv2.destroyAllWindows()

# 使用matplotlib
img = cv2.imread('test0.png', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]), # to hide tick values on X and Y axis
plt.show()
