import cv2
import numpy as np
img=cv2.imread('rgb.jpg')

img[0:112,0:200,2:3]=255
img[112:225,200:400,0:1]=255

img1=cv2.imread('autocon.jpg')
imgf=cv2.addWeighted(img,0.1,img1,0.8,0)
imshow('asd',imgf)

print(img.dtype)
cv2.waitKey(0)
cv2.destroyAllWindows()