import cv2 as cv
import numpy as np

#blank full screen
#blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

#green full screen
#blank[:] = 0,255,0
#cv.imshow('Green', blank)

#red zone screen
#blank[200:300, 300:400] = 255,0,0
#cv.imshow('Red Zone', blank)

#draw rectange
img = cv.imread('opencv/images/cat2.jpg')
blank = np.zeros((500,500,3), dtype='uint8')
blank[200:300, 300:400] = 255,0,0
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)

#draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3)

#draw line
cv.line(blank, (0,0), (200, 300), (255,255,255), thickness=3)

#draw line
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow('Red Zone', blank)

cv.waitKey(0)
