import numpy as np
import cv2
cap = cv2.VideoCapture(0)
img = 0
while True:
    ret, frame=cap.read()
    if ret:
        print(frame)
        img = frame
        break
cv2.imshow('frame',frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()               