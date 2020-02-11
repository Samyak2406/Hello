import cv2
import numpy as np
# def nothing(h):
#     pass
#cv2.namedWindow('image')

img=cv2.imread('WhatsApp Image 2019-11-25 at 6.10.04 PM.jpeg')
img[:,:,1]=0
img[:,:,0]=0
cv2.imshow('ch',img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret, mask = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) 


# cv2.createTrackbar('a','image',0,255,nothing)
# cv2.createTrackbar('s','image',0,255,nothing)
# cv2.createTrackbar('d','image',0,255,nothing)
# cv2.createTrackbar('z','image',0,255,nothing)
# cv2.createTrackbar('x','image',0,255,nothing)
# cv2.createTrackbar('c','image',0,255,nothing)

# while True:
#     # img=cv2.imread('chess.jpg')
#     # img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    


#     a = cv2.getTrackbarPos('a','image')
#     s = cv2.getTrackbarPos('s','image')
#     d = cv2.getTrackbarPos('d','image')
#     z = cv2.getTrackbarPos('z','image')
#     x = cv2.getTrackbarPos('x','image')
#     c = cv2.getTrackbarPos('c','image')


lower_blue = np.array([0,0,33])
upper_blue = np.array([255,255,255])
kernel = np.ones((6,6),np.uint8)
mask = cv2.inRange(mask, lower_blue, upper_blue)
mask = cv2.blur(mask,(3,3))

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

mask = cv2.erode(mask,kernel,iterations = 7)
#mask = cv2.blur(mask,(7,7))
mask = cv2.dilate(mask,kernel,iterations = 17)


# ret, mask = cv2.threshold(mask, 20, 100, cv2.THRESH_BINARY) 
mask=cv2.resize(mask,(400,400),interpolation=cv2.INTER_AREA)
#mask = cv2.Canny(mask,100,200)

mask = cv2.Canny(mask,100,200)
cv2.imshow('edges',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
