#Template matching


# import cv2
# import numpy as np


# template=cv2.imread('messi_face_template.jpg',0)
# img=cv2.imread('messipyr.jpg',0)
# img1=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

# cv2.imshow('try',img1)

# w,h=template.shape[::-1]

# result=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
# print(result)
# threshold=0.5
# loc=np.where(result>threshold)
# print(loc)
# for pt in zip(*loc[::-1]):
#    # print(pt)
#     cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(255,255,255),3)

# cv2.imshow('messi',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



#Haar cascade


import cv2
import numpy as np

face=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
cap=cv2.VideoCapture(0)


while True:
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,2,5)
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
    cv2.imshow('facedetect',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()