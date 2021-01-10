import cv2 as cv
import numpy as np

img = cv.imread('opencv/images/cat2.jpg')

cv.imshow('cat', img)

#translation
def translate(img, x, y):
    transMAt = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMAt, dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Left

translated = translate(img, -100, -100)
cv.imshow('Translated', translated) 

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions =(width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flip
flip = cv.flip(img, 0)
cv.imshow('Flipped',flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)