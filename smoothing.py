import cv2 as cv

img = cv.imread('images/cat1.webp')
cv.imshow('Original', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
M_blur = cv.medianBlur(img, 7)
cv.imshow('Median Blur', M_blur)

cv.waitKey(0)