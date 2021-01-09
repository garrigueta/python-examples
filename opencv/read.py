import cv2 as cv

#load image
img = cv.imread('opencv/images/cat3_large.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)

#load video
capture = cv.VideoCapture('opencv/videos/fog1.mp4')

while   True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()

cv.waitKey(0)