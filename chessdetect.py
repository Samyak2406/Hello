import cv2
import numpy as np
def nothing(h):
    pass
cv2.namedWindow('image')

img=cv2.imread('chess.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.createTrackbar('a','image',0,255,nothing)
cv2.createTrackbar('s','image',0,255,nothing)
cv2.createTrackbar('d','image',0,255,nothing)
cv2.createTrackbar('z','image',0,255,nothing)
cv2.createTrackbar('x','image',0,255,nothing)
cv2.createTrackbar('c','image',0,255,nothing)

while True:
    # img=cv2.imread('chess.jpg')
    # img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    


    a = cv2.getTrackbarPos('a','image')
    s = cv2.getTrackbarPos('s','image')
    d = cv2.getTrackbarPos('d','image')
    z = cv2.getTrackbarPos('z','image')
    x = cv2.getTrackbarPos('x','image')
    c = cv2.getTrackbarPos('c','image')


    lower_blue = np.array([a,s,d])
    upper_blue = np.array([z,x,c])

    mask = cv2.inRange(img, lower_blue, upper_blue)
#edges = cv2.Canny(img,100,200)
    cv2.imshow('edges',mask)
    cv2.waitKey(1500)
    cv2.destroyWindow('edges')
