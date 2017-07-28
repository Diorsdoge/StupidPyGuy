# -*- coding: utf-8 -*-

import cv2
import numpy as np 

img1 = cv2.imread('roi.jpg')

e1 = cv2.getTickCount()
for i in xrange(5, 49, 2):
	img1 = cv2.medianBlur(img1, i)

# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/cv2.getTickFrequency()
print t