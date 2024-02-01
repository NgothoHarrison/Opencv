import cv2 as cv
import numpy as np

img = cv.imread('images/rooster.png')[50:700, 200:900]
cv.imshow('Original', img)

# gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', gray)

# laplacian // edge detection 
lap = cv.Laplacian(gray, cv.CV_64F) # cv.CV_64F is the data type 
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)


# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)
