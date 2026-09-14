# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:32:19 2026

@author: ASUS
"""

import cv2

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
