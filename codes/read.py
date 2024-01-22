import cv2 as cv

#read images
img = cv.imread('photo/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)

#read videos
capture = cv.VideoCapture('video/10sec_video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
capture.destroyAllWindows()
