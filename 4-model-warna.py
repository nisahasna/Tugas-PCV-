# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:35:20 2026

@author: ASUS
"""

import cv2
import numpy as np

def rgb_to_cmyk(img_bgr):
    # Normalisasi RGB ke rantang 0-1
    bgr = img_bgr.astype(float) / 255.0
    B, G, R = bgr[:,:,0], bgr[:,:,1], bgr[:,:,2]
    
    K = 1 - np.maximum(np.maximum(R, G), B)
    C = (1 - R - K) / (1 - K + 1e-8)
    M = (1 - G - K) / (1 - K + 1e-8)
    Y = (1 - B - K) / (1 - K + 1e-8)
    
    cmyk = np.dstack((C, M, Y, K)) * 255
    return cmyk.astype(np.uint8)

def rgb_to_hsi(img_bgr):
    bgr = img_bgr.astype(float) / 255.0
    B, G, R = bgr[:,:,0], bgr[:,:,1], bgr[:,:,2]
    
    # Intensity
    I = (R + G + B) / 3.0
    
    # Saturation
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-8)) * min_rgb
    
    # Hue
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-8
    theta = np.arccos(np.clip(num / den, -1.0, 1.0))
    
    H = np.zeros_like(R)
    H[B > G] = 2 * np.pi - theta[B > G]
    H[B <= G] = theta[B <= G]
    H = H / (2 * np.pi) # Normalisasi H ke [0, 1]
    
    hsi = np.dstack((H * 255, S * 255, I * 255))
    return hsi.astype(np.uint8)

img = cv2.imread('data/chikawa.jpg')

if img is not None:
    # 1. BGR to HSV (Menggunakan OpenCV)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 2. BGR to CMYK (Custom Function)
    cmyk = rgb_to_cmyk(img)
    
    # 3. BGR to HSI (Custom Function)
    hsi = rgb_to_hsi(img)

    cv2.imshow('Original (BGR)', img)
    cv2.imshow('HSV Color Space', hsv)
    cv2.imshow('CMYK (Channel C,M,Y)', cmyk[:,:,:3])
    cv2.imshow('HSI Color Space', hsi)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()