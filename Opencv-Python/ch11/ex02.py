# -*- coding: utf-8 -*-

import cv2
import numpy as np 

# check if opetimization is enabled
In [5]: cv2.useOptimized()
Out[5]: True

In [6]: %timeit res = cv2.medianBlur(img, 49)

# Disable it
In [7]: cv2.setUseOptimized(False)

In [8]: cv2.useOptimized()
Out[8]: False
In [9]: %timeit res = cv2.medianBlur(img, 49)

In [10]: x = 5

In [11]: %timeit y = x**2

In [12]: %timeit y=x*x 

In [15]: z = np.uint8([5])

In [17]: %timeit y=z*z

In [19]: %timeit y=np.square(z)

In [35]: %timeit z = cv2.countNoZero(img)

In [36]: %timeit z = np.count_nonzero(img)

# OpenCV 的函数是 Numpy 函数的 25 倍