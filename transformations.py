import cv2 as cv
import numpy as np

img = cv.imread('/Users/bhaskar/Downloads/rainy_image_dataset/training/ground_truth/1.jpg')

cv.imshow('Original', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated image', translated)

#rotation
def rotation(img,angle,rotPoint = None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotation(img, 20)
cv.imshow('ROtated', rotated)


#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


#flipping
flipped = cv.flip(img, -1)
cv.imshow('Flip', flipped)



cv.waitKey(0)