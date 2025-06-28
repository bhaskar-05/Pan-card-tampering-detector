#we gonna take an image and split it into its 3 color channels

import cv2 as cv
import numpy as np

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank, r])

cv.imshow('Bluee',blue)
cv.imshow('Greeen',green)
cv.imshow('Reed',red)

cv.imshow('Blue', b)
cv.imshow('Green',g)
cv.imshow('Red',r)

merged = cv.merge([b,g,r])

cv.imshow('Merged', merged)

cv.waitKey(0)