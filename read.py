import cv2 as cv
import sys
import rescale_video as rv

# Reading images
img = cv.imread('images/cat1.webp')
# img = cv.imread('images/dog3.jpeg')
if img is None:
    sys.exit('Could not read the image.')

cv.imshow('Cat Image', img)
# cv.imshow('Dog Image', img)

cv.waitKey(0) # 0 means infinite time, the image will be shown until we press any key

# Reading videos

capture = cv.VideoCapture('videos/video4.mp4')

cv.imshow('Video', capture)
rv.rescaleFrame(capture) # the impoted module to rescale videos
