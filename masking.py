import cv2 as cv
import numpy as np

img = cv.imread('images/cat1.webp') 
cv.imshow('Original', img)

blank =np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

# masking --> masking is used to focus on a certain part of the image 
# masking is used to hide certain parts of the image

# making a circle mask on the blank generated image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 ), 100,255, -1)
cv.imshow('Mask', mask)

# masking the image loaded to the drawn circle mask
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)



cv.waitKey(0)