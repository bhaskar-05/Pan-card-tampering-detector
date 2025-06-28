import cv2 as cv
import numpy as np

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')
cv.imshow('original', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

contours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#drawing the contours
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

print(len(contours))

cv.waitKey(0)