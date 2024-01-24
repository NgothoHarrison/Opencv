import cv2 as cv
import numpy as np
import sys

# Convert an image to grayscale
img = cv.imread('images/cat1.webp')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)