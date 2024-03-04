import cv2 as cv
""" 
# deal with images # 原始資料
img = cv.imread('photo\cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale # 灰階處裡
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

# blur # 模糊化
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur) 

# edge cascade # canny 邊緣檢測
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# dilating the image # 邊緣延伸
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilate', dilated)

cv.waitKey(0)
 """

# deal with video formats
capture = cv.VideoCapture('video/min_10sec_video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Capture', frame)

    # converting to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # blur
    blur = cv.GaussianBlur(frame, (0, 0), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)  
    
    # edge cascade
    canny = cv.Canny(frame, 125, 175)
    cv.imshow('Canny', canny)

    # dilating the image # 邊緣延伸
    dilated = cv.dilate(canny, (7, 7), iterations=3)
    cv.imshow('Dilate', dilated)


    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
capture.destroyAllWindows() 
