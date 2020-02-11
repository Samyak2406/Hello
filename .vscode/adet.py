# import cv2
# import numpy as np
# img=cv2.imread('WhatsApp Image 2019-11-25 at 6.10.04 PM.jpeg')
# # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# temp = img.copy()
# img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
# lower_blue = np.array([0,0,60])
# upper_blue = np.array([255,255,240])
# kernel = np.ones((6,6),np.uint8)
# mask = cv2.inRange(img, lower_blue, upper_blue)
# mask = cv2.blur(mask,(3,3))
# erosion = cv2.erode(img,kernel,iterations = 15)

# blur = cv2.blur(mask,(5,5))

# mask = cv2.bitwise_or(mask,blur)
# mask = cv2.erode(mask,kernel,iterations = 1)
# #erosion = cv2.erode(img,kernel,iterations = 15)
# mask= cv2.dilate(mask,kernel,iterations = 3)
# # mask = cv2.bitwise_and(mask,gray)
# mask=cv2.resize(mask,(400,400),interpolation=cv2.INTER_AREA)
# temp=cv2.resize(temp,(400,400),interpolation=cv2.INTER_AREA)
# contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     cv2.drawContours(temp, cnt,0,color=(0,0,255),thickness=3)




# cv2.imshow('+=+',temp)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






# import cv2
# import numpy as np
# img=cv2.imread('WhatsApp Image 2019-11-25 at 6.10.04 PM.jpeg')

# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,25,255,0)

# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# img = cv2.drawContours(img, contours, -1, (0,255,0), 1)
# img=cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
# cv2.imshow('asd',img)
# thresh=cv2.resize(thresh,(400,400),interpolation=cv2.INTER_AREA)

# cv2.imshow('asd1',thresh)

# median = cv2.medianBlur(thresh,3)
# cv2.imshow('asd2',median)
# kernel = np.ones((3,3),np.uint8)

# opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
# cv2.imshow('ads2.5',opening)
# kernel = np.ones((7,7),np.uint8)
# dilation = cv2.dilate(median,kernel,iterations = 1)
# cv2.imshow('ads3',dilation)
# contourss, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# imgx = cv2.drawContours(dilation, contourss, -1, (0,255,0), 10)
# cv2.imshow('asd4',imgx)



# cv2.waitKey(0)





import cv2
import numpy as np
img=cv2.imread('5.jpg')
imgx=cv2.imread('6.jpg')
img=cv2.resize(img,(600,600),interpolation=cv2.INTER_AREA)
imgx=cv2.resize(imgx,(600,600),interpolation=cv2.INTER_AREA)

img= cv2.bilateralFilter(img, 7, 150, 85) 
cv2.imshow('asdfg',img)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,56,255,1)
thr1=thresh
kernel = np.ones((6,6),np.uint8)
thresh= cv2.dilate(thresh,kernel,iterations = 1)
cv2.imshow('qwert',thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
thresh = cv2.drawContours(img, contours, -1, (75,20,255), 3)








imgx= cv2.bilateralFilter(imgx, 7, 150, 85) 
cv2.imshow('asdfzzzg',imgx)

imgrayx = cv2.cvtColor(imgx,cv2.COLOR_BGR2GRAY)
ret,threshx = cv2.threshold(imgrayx,56,255,1)
thr2=threshx
kernel = np.ones((6,6),np.uint8)
threshx= cv2.dilate(threshx,kernel,iterations = 1)
cv2.imshow('qwzzert',threshx)
contoursx,hierarchy = cv2.findContours(threshx, 1, 2)
threshx = cv2.drawContours(imgx, contoursx, -1, (75,20,255), 3)
cv2.imshow('zzzz',imgx)

imgg=thr2-thr1
cv2.imshow('poiu',imgg)

#cv2.imshow('1',img)
cv2.imshow('1.1',thresh)
cv2.waitKey(0)

