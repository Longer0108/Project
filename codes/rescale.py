import cv2 as cv

def rescaleFrame(frame, scale=0.75): # for all (like images, videos, lives)
    width = int(frame.shape[1] * scale) # video_width
    height = int(frame.shape[0] * scale) # video_height

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height): #only for live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('video/10sec_video.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.3)

    #cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
capture.destroyAllWindows() 