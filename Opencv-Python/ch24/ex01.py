# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../messi5.jpg', 0)
img2 = img.copy()
template = cv2.imread('messi_face.jpg', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
	img = img2.copy()

	# exec 语句用来执行储存在字符串或文件中的Python语句
	# 例如 我们可以在  时生成一个包含 Python 代码的字符串 然后使用 exec  句执  些 句。 
	# eval  句用来 算存储在字符串中的有效 Python   式
	method = eval(meth)

	# Apply template Mathching
	res = cv2.matchTemplate(img, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	# 使用不同的比较方法，对结果的解释不同

	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: 
		top_left = min_loc
	else:
		top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
