"""
3-filter-spasial.py
Penerapan filter spasial: konvolusi manual, smoothing (mean, gaussian),
median, serta penajaman (laplacian, sobel).
"""
import cv2
import numpy as np

img = cv2.imread('data/chikawa.jpg')

if img is not None:
    # 1. Smoothing / Mean Filter (Low Pass Filter)
    kernel_blur = np.ones((5, 5), np.float32) / 25
    blur_img = cv2.filter2D(img, -1, kernel_blur)
    
    # 2. Gaussian Blur
    gaussian_img = cv2.GaussianBlur(img, (5, 5), 0)
    
    # 3. Sharpening Filter (High Pass Filter)
    kernel_sharpening = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    sharpened_img = cv2.filter2D(img, -1, kernel_sharpening)
    
    # 4. Sobel Edge Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(sobel_combined)

    cv2.imshow('Original Image', img)
    cv2.imshow('Mean Blur', blur_img)
    cv2.imshow('Gaussian Blur', gaussian_img)
    cv2.imshow('Sharpened Image', sharpened_img)
    cv2.imshow('Sobel Edge Detection', sobel_combined)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()