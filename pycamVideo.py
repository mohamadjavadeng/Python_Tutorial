import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if ret:
        output.write(frame)
        cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
output.release()
cv.destroyAllWindows()