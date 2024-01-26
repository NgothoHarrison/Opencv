import cv2 as cv
import numpy as np

img = cv.imread('images/cat1.webp')

cv.imshow('Original image', img)

# Translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # this is the translation matrix
    dimensions = (image.shape[1], image.shape[0]) # this is the dimensions of the image
    return cv.warpAffine(image, transMat, dimensions) # this is the translation function

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# key points:
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # this is the height and width of the image

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # this is the rotation matrix
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow('Rotated', rotated)

# double_rotated = rotate(rotated, 45)
# cv.imshow('Double Rotated', double_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC) # the second argument is the new dimensions of the image
cv.imshow('Resized', resized) 

# Flipping
flip = cv.flip(img, 0)
cv.imshow('Flipped', flip)

# Cropping
cropped = img[100:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)