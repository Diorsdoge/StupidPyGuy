# -*- coding: utf-8 -*-

import numpy as np 
import cv2

img = cv2.imread('star.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

# 图像的矩可以计算图像的质心
cnt = contours[0]
M = cv2.moments(cnt)
print M

# 计算对象的重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


# 轮廓面积
area = cv2.contourArea(cnt)

# 轮廓周长
perimeter = cv2.arcLength(cnt, True)

# 轮廓近似
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

# 凸包   points——传入的轮廓， hull——输出， clockwise——方向标志true顺时针false逆时针，returnpoints——默认为true返回凸包点坐标
hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]])
hull = cv2.convexHull(cnt)

# 凸性检测
k = cv2.isContourConvex(cnt)

# 边界矩形
# 直边界矩形
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0),2)
# 旋转边界矩形
img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0),2)

# 最小外接圆
(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0,255,0),2)

# 椭圆拟合
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im, ellipse, (0,255,0),2)

# 直线拟合
rows, cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx)+y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img, (cols-1, righty), (0, lefty), (0,255,0),2)

# 长宽比
w,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

# Extent 轮廓面积与边界矩形面积比
area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area

# Solidity 轮廓面积与凸包面积的比
area = cv2.contourArea(cnt)
hull = CV2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

# Equivalent Diameter 与轮廓面积相等的圆形的直径
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# 方向
(x,y), (MA,ma),angle = cv2.fitEllipse(cnt)

# 掩模核像素点
mask = np.zeros(imgray.shape, np.uint8)
cv2.drawContours(mask, [cnt],0,255,-1)
pixelpoints= np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)

# 最大值，最小值及他们的位置
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(imgray, mask = mask)

# 平均颜色及平均灰度
mean_val = cv2.mean(im, mask = mask)

# 极点，最上，最下，最左，最右的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# 凸缺陷
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)


