""" import numpy as np
import cv2
img=cv2.imread('test.jpg',cv2.IMREAD_UNCHANGED)
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.imshow('img',img)
cv2.waitKey(0) """

import cv2
import time
import os
import sys

workpath=os.path.dirname(sys.argv[0])
os.chdir(workpath)          #指定py文件执行路径为当前工作路径

def getnowtime():
    mstime=int(1000*time.time())
    print(mstime)
    return mstime
#引入库
num = 0
cap = cv2.VideoCapture(-1)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    savename=str(getnowtime())+'.jpg'
    cv2.imwrite(savename,frame)
    cv2.waitKey(1000/33)
    num = num +1
#读取内容
    if cv2.waitKey(10) == ord("e"):
        break
    if num > 20:
        break

        
#随时准备按q退出
cap.release()
cv2.destroyAllWindows()
#停止调用，关闭窗口