# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:37:35 2026

@author: ASUS
"""

import cv2
import numpy as np

img = cv2.imread('data/chikawa.jpg', cv2.IMREAD_GRAYSCALE)

if img is not None:
    # Thresholding citra ke bentuk biner
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Structuring Element / Kernel (3x3)
    kernel = np.ones((3, 3), np.uint8)
    
    # 1. Erosi
    erosion = cv2.erode(binary_img, kernel, iterations=1)
    
    # 2. Dilasi
    dilation = cv2.dilate(binary_img, kernel, iterations=1)
    
    # 3. Opening (Erosi diikuti Dilasi)
    opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
    
    # 4. Closing (Dilasi diikuti Erosi)
    closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Binary Image', binary_img)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()