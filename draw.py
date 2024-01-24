import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # This is a black image   
cv.imshow('Blank', blank)

# color is in the BGR format
blank[:] = 0, 165, 255 # This will paint the whole image green
blank[200:300, 300:400] = 0,0,255 # This will paint a part of the IMAGE red 
blank[50:100, 100:200] = 255,0,0 # This will paint a part of the IMAGE blue
cv.imshow('Green', blank)

# Draw a rectangle
rectangle = cv.rectangle(blank, (0,0), (250,250), (0,0,0), thickness=2) # define the image, the starting point, the ending point, the color and the thickness
rectangle = cv.rectangle(blank,(100,100), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 0), thickness = -1 )# thickness = -1 will fill the rectangle
cv.imshow('Draw Rectangle', rectangle)

# draw a circle
circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (255,0,255), thickness=3) # define the image, the center point, the radius, the color and the thickness
cv.imshow('Draw Circle', circle)

# draw a line
line = cv.line(blank, (50,50), (450,450), (255,255,255), thickness=3) # define the image, the starting point, the ending point, the color and the thickness
cv.imshow('Draw Line', line)

# write text on an image
cv.putText(blank, 'Made with love by Hank', (80,400), cv.FONT_HERSHEY_SIMPLEX, 1.0, (208, 224, 64), thickness=3)
cv.imshow('Draw Text', blank)

img = cv.imread('images/cat1.webp' )

cv.imshow('Draw Cat', img)

cv.waitKey(0)