import cv2 as cv

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')
cv.imshow('Bird', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#canny
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated',  dilated)

#eroding the image
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('resized', resized)

#cropped
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)