import cv2 as cv
import numpy as np


def rescaleFrame(frame): # for all (like images, videos, lives)
    width = int(640) # video_width
    height = int(400) # video_height

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height): #only for live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('video/10sec_video.mp4')
frame_count = 0  # 新增一個計數器

fourcc = cv.VideoWriter_fourcc(*'mp4v')          # 設定影片的格式為 MJPG 
# 如果是 mov 或 mp4 的影片檔，使用「＊'mp4v'」、「＊'MJPG'」或「'M','J','P','G'」
out = cv.VideoWriter('video/min_10sec_video.mp4', fourcc, 20.0, (640,  400))  # 產生空的影片

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    # 將取得的每一幀圖像寫入空的影片
    out.write(frame_resized)
    
    #cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

out.release()      # 釋放資源
capture.release()
capture.destroyAllWindows() 