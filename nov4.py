import cv2
import numpy as np
def nothing(q):
    
    pass

# img=cv2.imread('autocon.jpg',cv2.IMREAD_UNCHANGED)
# nwimg=cv2.resize(img,(90,90),interpolation=cv2.INTER_AREA)
# cv2.imshow('resize',nwimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(nwimg.shape)

cv2.namedWindow('hsv')

cv2.createTrackbar('L1','hsv',0,255,nothing)
cv2.createTrackbar('H1','hsv',0,255,nothing)
cv2.createTrackbar('L2','hsv',0,255,nothing)
cv2.createTrackbar('H2','hsv',0,255,nothing)
cv2.createTrackbar('L3','hsv',0,255,nothing)
cv2.createTrackbar('H3','hsv',0,255,nothing)
    


cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    L1=cv2.getTrackbarPos('L1','hsv')
    H1=cv2.getTrackbarPos('H1','hsv')
    L3=cv2.getTrackbarPos('L3','hsv')
    H2=cv2.getTrackbarPos('H2','hsv')
    L2=cv2.getTrackbarPos('L2','hsv')
    H3=cv2.getTrackbarPos('H3','hsv')

    mask=cv2.inRange(hsv,np.array([L1,L2,L3]),np.array([H1,H2,H3]))
    res = cv2.bitwise_and(frame,frame, mask= mask)
    mask1=cv2.medianBlur(mask,3)

    kernel=np.ones((4,4),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    cv2.imshow('org',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('solo',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()




    
   


