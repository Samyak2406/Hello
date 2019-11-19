import cv2
import numpy as np

def nothing(q):
	pass

pic=cv2.imread('autocon.jpg')
#pic=cv2.GaussianBlur(pic,(51,51),0)
cv2.namedWindow('name')


pic=cv2.resize(pic,(800,800),interpolation=cv2.INTER_AREA)
cpic=pic
pic=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
#laplacian = cv2.Laplacian(pic,cv2.CV_64F)
#kernel=np.ones((8,8),np.uint8)
# pic=cv2.erode(pic,kernel,iterations=1)
#npic = cv2.Laplacian(pic,cv2.CV_64F)
cv2.createTrackbar('a','name',0,1500,nothing)
cv2.createTrackbar('b','name',0,1500,nothing)
while True:
	a=cv2.getTrackbarPos('a','name')
	b=cv2.getTrackbarPos('b','name')
	npic=cv2.Canny(pic,a,b)
	cv2.imshow('npic',npic)
	cv2.waitKey(3000)
	cv2.destroyWindow('npic')







#npic = cv2.morphologyEx(npic, cv2.MORPH_CLOSE, kernel)


cv2.imshow('pic',cpic)
cv2.waitKey(0)
cv2.destroyAllWindows()

l