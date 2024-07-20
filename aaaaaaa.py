import glob
import os
import cv2
import numpy as np

def isComapre(img1, img2):
    h = img1.shape[0]
    w = img1.shape[1]
    diff=cv2.subtract(img1,img2)
    x = np.sum(diff**2)
    error = (x) / h * w
    return error

res=False
path = "D:\sakshi\\"
image = cv2.imread("abc.jpg", cv2.IMREAD_COLOR)
data_path = os.path.join(path,'*g') 
files = glob.glob(data_path) 
for f1 in files: 
    img = cv2.imread(f1)
    if(isComapre(img,image)):
        res=True
if res:
    print("found")
else:
    print("not found")