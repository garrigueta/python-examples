import cv2 as cv

img = cv.imread('opencv/images/cat2.jpg')

cv.imshow('Cat2', img)

#convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('CatGrayed', gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

cv.imshow('CatBurred', blur)

#edge cascade
cany = cv.Canny(img, 125, 175)

cv.imshow('CatEdged', cany)

#dilating an image
dilated = cv.dilate(img, (7,7), iterations=3)

cv.imshow('CatDilated', dilated)

#eroding
eroded = cv.erode(img, (7,7), iterations=3)

cv.imshow('Cat', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

cv.imshow('Cat3', resize)

#crop
cropped = img[50:200, 200:400]

cv.imshow('Cat4', cropped)

cv.waitKey(0)