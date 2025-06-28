import cv2 as cv
import numpy as np

img = cv.imread('/Users/bhaskar/Desktop/BIT-Restaurant/1.jpg')
cv.imshow('1', img)

#creating a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1. painting the image a certain color
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)

#2. Drawing a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# #4. Draw a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0),thickness=1 )
cv.imshow('Line', blank)

#5 Write a text
cv.putText(blank, 'Hellow', (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)