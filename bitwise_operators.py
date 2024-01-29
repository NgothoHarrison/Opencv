import cv2 as cv
import numpy as np

blank = np.zeros((400, 400)) # blank image
cv.imshow('Blank', blank)

# Draw a rectangle

rectangle = cv.rectangle(blank.copy(), (30,30) , (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)

circle = cv.circle(blank.copy(), (200,200) , 200, 255 , -1)
cv.imshow('Circle', circle)

# Bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR --> Non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR --> Non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('BITWISE XOR', bitwise_xor)

# Bitwise NOT // Inverts the binary color 
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)


cv.waitKey(0)