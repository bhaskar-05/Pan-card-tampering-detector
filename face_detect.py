import cv2 as cv

img = cv.imread('/Users/bhaskar/Downloads/ladyy.jpeg')
cv.imshow('Lady', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)