import cv2 as cv
import rescale_video as rv

# Reading images
img = cv.imread('images/cat1.webp')
# img = cv.imread('images/dog3.jpeg')

cv.imshow('Cat Image', img)
# cv.imshow('Dog Image', img)

cv.waitKey(0) # 0 means infinite time, the image will be shown until we press any key

# Reading videos

capture = cv.VideoCapture('videos/video4.mp4')

cv.imshow('Video', capture)
rv.rescaleFrame(capture) # the impoted module to rescale videos



# Rescaling images and videos
# def rescaleFrame(frame, scale=0.2):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width,height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video', frame)
#     cv.imshow('video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'): # 0xFF==ord('d') is used to stop the video when we press 'd' key
#         break

# capture.release()
# cv.destroyAllWindows()