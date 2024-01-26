import cv2 as cv

img = cv.imread('images/cat1.webp')
cv.imshow('Original', img)

# Splitting the image into its color channels
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging the color channels

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)