import cv2 as cv
import numpy as np
import sys

img = cv.imread('images/cat1.webp')
cv.imshow('Original', img)


# Convert an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # the second argument is the kernel size, it has to be an odd number
cv.imshow('Blur', blur) 

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # the second and third arguments are the threshold values
# canny = cv.Canny(img, 125, 175) # this has more details than the blured version
cv.imshow('Canny Edges', canny)

# Dilating the image // makes the edges thicker
dilated = cv.dilate(canny, (7,7), iterations=3) # // iterations is the number of times we want to dilate the image
cv.imshow('Dilated', dilated)

# Eroding // makes the edges thinner
eroded = cv.erode(dilated, (7,7), iterations=2)
cv.imshow('Eroded', eroded) # this will be the same as the canny image since the parameters are the same

# Resize an image
resized = cv.resize(img, (500,400), interpolation=cv.INTER_CUBIC) # the second argument is the new dimensions of the image
cv.imshow('Resized', resized)

# Cropping an image
cropped = img[50:200, 100:400] # the first argument is the height and the second is the width
cv.imshow('Cropped', cropped)

# 


cv.waitKey(0)