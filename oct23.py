# import cv2
# import numpy

# img=cv2.imread('rgb.jpg')
# #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img[0:225,:400,2:3] =0
# cv2.imshow('blue+green frames only',img)
# cv2.waitKey(0)






# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # print(img.shape)
# import cv2
# import numpy
# img=cv2.imread('rgb.jpg')
# img[:,:,2]=0
# cv2.imshow('same here',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






# import cv2
# import numpy as np
# img1=cv2.imread('rgb.jpg')
# img1[0:225,0:400,:]=img1[0:225,0:400,:]*0.6
# cv2.imshow('weighted',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()














import cv2
import numpy as np
img=cv2.imread('rgb.jpg')
img[0:112,0:200,1:3]=0
img[112:225,200:400,0:2]=0
cv2.imshow('half',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





