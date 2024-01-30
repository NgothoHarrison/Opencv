import cv2 as cv
import numpy as np

# thresholding --> thresholding is used to seperate the foreground from the background

img = cv.imread('images/rooster.png')
img = img[50:700, 200:900]              # img[height, width]
cv.imshow('Original', img)

# gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# simple thresholding inverse
threshold, thresh_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# adaptive thresholding
# adaptive thresholding is used to seperate the foreground from the background when the image has different lighting conditions
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)