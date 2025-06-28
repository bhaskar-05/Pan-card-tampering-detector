import cv2 as cv
import numpy as np

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')
cv.imshow('Original', img)

#Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#gaussian blur

#median blur
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

#bilateral blurring, applies blurring but retains edges as well
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)