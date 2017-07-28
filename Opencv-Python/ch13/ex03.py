# -*- codeing: utf-8 -*-

import cv2
import numpy as np

# green = np.uint8([0, 255, 0])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

# 所以不能用 [0,255,0],而要用 [[[0,255,0]]]
# 这里的三层括号应该分别对应于 cvArray,cvMat,IplImage

green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print hsv_green