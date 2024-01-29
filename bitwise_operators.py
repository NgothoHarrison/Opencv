import cv2 as cv
import numpy as np

blank = np.zeros((400, 400)) # blank image
cv.imshow('Blank', blank)

# Draw a rectangle

rectangle = cv.rectangle(blank.copy(), (30,30) , (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

circle = cv.circle(blank.copy(), (200,200) , 200, 255 , -1)
cv.imshow('Circle', circle)


cv.waitKey(0)