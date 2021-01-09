import cv2 as cv

def changeRes(width, height):
    #for live video purposes
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.5):
    # images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)

#load video
capture = cv.VideoCapture("opencv/videos/fog1.mp4")

while   True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.waitKey(0)