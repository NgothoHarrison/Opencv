import cv2 as cv
import numpy as np

img = cv.imread('images/cat1.webp') 
cv.imshow('Original', img)

blank =np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

# masking --> masking is used to focus on a certain part of the image 
# masking is used to hide certain parts of the image

# making a circle mask on the blank generated image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 ), 100,255, -1)
cv.imshow('Mask', mask)

# masking the image loaded to the drawn circle mask
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

# rectangle mask 
rectangle = cv.rectangle(blank.copy(), (30,30) , (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

# masking the image loaded to the drawn rectangle mask
rect_masked = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Rectangle Masked Image', rect_masked)

# Triangle mask
inverse = np.zeros(img.shape[:2], dtype='uint8')
inverse = cv.bitwise_not(cv.circle(inverse, (img.shape[1]//2, img.shape[0]//2 ), 100,255, -1))
cv.imshow('Inverse', inverse)


inverse_mask = cv.bitwise_and(img, img, mask=inverse)
cv.imshow('Inversed Masked Image', inverse_mask)

cv.waitKey(0)