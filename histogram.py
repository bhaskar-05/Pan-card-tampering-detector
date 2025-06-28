import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank= np.zeros(img.shape[:2], dtype = 'uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask = circle) 
cv.imshow('Masked', mask)


#grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256],[0,256])

cv.waitKey(0)