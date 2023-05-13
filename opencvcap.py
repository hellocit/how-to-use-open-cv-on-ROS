#!/usr/bin/env python3

import cv2

deviceid=4 # it depends on the order of USB connection. 
capture = cv2.VideoCapture(deviceid)

ret, frame = capture.read()
cv2.imwrite('test.jpg', frame)