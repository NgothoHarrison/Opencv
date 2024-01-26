import cv2 as cv 

# contours are the boundaries of an object
# they are useful for shape analysis and object detection and recognition
img = cv.imread('images/cat1.webp')
cv.imshow('Original', img)

# Convert an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an image
blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT) # the second argument is the kernel size, it has to be an odd number
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(gray, 125,175)
cv.imshow("Canny Edges", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # the second argument is the retrieval method and the third is the approximation method
# RETR_LIST --> retrieves all the contours
# RETR_EXTERNAL --> retrieves only the external contours
# RETR_TREE --> retrieves all the contours and creates a full family hierarchy list
# RETR_CCOMP --> retrieves all the contours and organizes them into a two-level hierarchy
# CHAIN_APPROX_NONE --> stores all the boundary points
print(f'{len(contours)} countour(s) found!')

cv.waitKey(0)