import cv2 as cv

img = cv.imread('images/cat1.webp')
cv.imshow('Original', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)


cv.waitKey(0)