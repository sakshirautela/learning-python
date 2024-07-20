import cv2
import os
from cv2 import INTER_LINEAR
import numpy as np


def isComapre(img1, img2):
    h = img1.shape[0]
    w = img1.shape[1]
    if(img1.shape!=img2.shape):
        return 100000000000000000000000000000
    diff=cv2.subtract(img1,img2,dtype=cv2.CV_64F)
    x = np.sum(diff**2)
    error = (x) / h * w
    print(error)
    return error


def getPath(path):
    list =[]
    for x in os.listdir(path):
        list.append(x)
    return(list)


def getImage(list):
    images=[]
    for i in list:
        a=cv2.imread(os.path.join(path,i))
        read=cv2.resize(a,(1000,1000),interpolation=INTER_LINEAR)
        if read is not None:
            images.append(read)
    return images


if __name__ == '__main__':
    asread = cv2.imread("example.jpg", cv2.IMREAD_COLOR)
    sample=cv2.resize(asread,(1000,1000),interpolation=INTER_LINEAR)

    path = "D:\sakshi\\"
    list=getPath(path)
    image=getImage(list)
    
    result=False
    for i in image:
        if(isComapre(sample,i)<3433339795.0):
            result=True
            break
    if result:
        print("found image")
    else:
        print("not found image")
