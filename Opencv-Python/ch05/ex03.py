# -*- coding: utf-8 -*-

import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
w = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
# Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(w), int(h)))

while cap.isOpened():
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame, 0)

		# write the filpped frame
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()