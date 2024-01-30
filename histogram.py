import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/rooster.png')
img = img[50:500, 200:900]              # img[height, width]
cv.imshow('Original', img)


# gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', gray)

# histogram --> a graphical representation of the intensity distribution of an image
# grayscale histogram

gray_hist = cv.calcHist([gray],[0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# color histogram
# color histogram is used to find the dominant color in the image

colors = ('b', 'g', 'r')
for i , col in enumerate(colors):
    hist =cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()




cv.waitKey(0)