import cv2
import chess
import numpy as np
ls1=ls2=ls=[]
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        ls.append([x,y])

#ls11=[[7, 6], [68, 7], [126, 5], [189, 8], [249, 7], [311, 8], [370, 6], [432, 5], [493, 6], [6, 67], [67, 67], [128, 67], [188, 66], [249, 68], [310, 69], [371, 68], [432, 67], [492, 66], [7, 128], [66, 129], [129, 128], [190, 126], [249, 129], [310, 129], [372, 128], [432, 128], [494, 127]]
ch=cv2.imread('bwibchessboard.png',0)
ch=cv2.resize(ch,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow('cb',ch)
while True:
    cv2.setMouseCallback('cb',draw_circle)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(ls)
#if [7,6] in ls11:
#    print('i support sql')
#ch=np.array(ch)
# print(np.where(a==7))
cv2.destroyAllWindows()


