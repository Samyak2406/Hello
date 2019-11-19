import cv2
import numpy as np
img=cv2.imread('DSC_0018.JPG')
img=cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img11',gray)

_,gray = cv2.threshold(gray,50,150,0)
cv2.imshow('img1',gray)


canny=cv2.Canny(gray,100,300)
contours,nouse=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cnt = contours[1]
M = cv2.moments(cnt)
print(M) 
cx = int(M['m10']/M['m00'])
print(cx)
cv2.imshow('img13',canny)


img = cv2.drawContours(img, contours, -1, (0,255,0), 1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
