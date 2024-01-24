import cv2 as cv
import numpy as np
import sys

# Convert an image to grayscale
img = cv.imread('images/cat1.webp')
cv.imshow('Cat', img)

cv.waitKey(0)