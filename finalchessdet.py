import cv2
import numpy as np
img=cv2.imread('WhatsApp Image 2019-11-25 at 6.10.04 PM.jpeg')
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
temp = img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
lower_blue = np.array([0,0,60])
upper_blue = np.array([255,255,240])
kernel = np.ones((6,6),np.uint8)
mask = cv2.inRange(img, lower_blue, upper_blue)
mask = cv2.blur(mask,(3,3))
erosion = cv2.erode(img,kernel,iterations = 15)

blur = cv2.blur(mask,(5,5))

mask = cv2.bitwise_or(mask,blur)
mask = cv2.erode(mask,kernel,iterations = 1)
#erosion = cv2.erode(img,kernel,iterations = 15)
mask= cv2.dilate(mask,kernel,iterations = 3)
# mask = cv2.bitwise_and(mask,gray)
mask=cv2.resize(mask,(400,400),interpolation=cv2.INTER_AREA)
temp=cv2.resize(temp,(400,400),interpolation=cv2.INTER_AREA)
contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(temp, cnt,0,color=(0,0,255),thickness=3)




cv2.imshow('+=+',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()