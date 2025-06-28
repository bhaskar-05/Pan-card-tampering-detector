import cv2 as cv
# img = cv.imread('/Users/bhaskar/Downloads/carbon.png')
# cv.imshow('carbon',img)
# cv.waitKey(0)

#rezizing image, video, live video
def rescaleFrame(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#resizing live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4,height)

#reading videos
capture = cv.VideoCapture('/Users/bhaskar/Downloads/Superman and Lois S04E09 To Live and Die Again 1080p AMZN WEB-DL DDP5 1 H 264-FLUX[TGx]/Superman and Lois S04E09 To Live and Die Again 1080p AMZN WEB-DL DDP5 1 H 264-FLUX.mkv')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,0.2)
    cv.imshow('Video', frame)
    cv.imshow('Resized_video', frame_resized)

    if(cv.waitKey(20) & 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()
