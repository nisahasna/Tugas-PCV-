# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:09:45 2026

@author: ASUS
"""

import cv2
import numpy as np

image = cv2.imread('data/chikawa.jpg')
[h,w,c] = image.shape

for i in range(h):
    for j in range(w):
        image[i,j,1] = 0
        image[i,j,2] = 0
        
cv2.imshow("Chikawa Biru", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            frame[i,j,0] = 0
            frame[i,j,1] = 0
    
    cv2.imshow('Frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
