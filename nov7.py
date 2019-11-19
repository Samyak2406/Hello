import cv2
import numpy as np
img=cv2.imread('DSC_0018.JPG')
img1=cv2.imread('DSC_0020.JPG')
img1=cv2.resize(img1,(400,400),interpolation=cv2.INTER_AREA)
gray1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img11',gray)

#_,gray = cv2.threshold(gray,50,150,0)
# cv2.imshow('img1',gray)



canny=cv2.Canny(gray,100,300)
contours,nouse=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
canny1=cv2.Canny(gray1,100,300)
contours1,nouse1=cv2.findContours(canny1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
ret = cv2.matchShapes(contours[5],contours1[5],1,0.0)
print(ret)



#print(len(contours))
# cnt = contours[10]
# M = cv2.moments(cnt)
# print(M) 
#cx = int(M['m10']/M['m00'])
#print(cx)
# cv2.imshow('img13',canny)
# perimeter = cv2.arcLength(cnt,True)
# print(perimeter)
# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)
# cv2.imshow('eps',approx)




# img = cv2.drawContours(img, contours, 30, (0,255,0),2)
# cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
