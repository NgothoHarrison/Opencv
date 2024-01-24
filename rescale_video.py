import cv2 as cv

capture = cv.VideoCapture('videos/video4.mp4')

# to change resolution
# only works for LIVE VIDEOS
def changeResolution(width,height):
    capture.set(3,width)
    capture.set(4,height)

# Rescaling images and videos
# The method works for IMAGES, VIDEOS and LIVE VIDEOS
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame) # This is the original video
    cv.imshow('video Resized', frame_resized) # This is the resized video

    if cv.waitKey(20) & 0xFF==ord('d'): # 0xFF==ord('d') is used to stop the video when we press 'd' key
        break

capture.release()
cv.destroyAllWindows()