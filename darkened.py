import cv2
import numpy as np

def  minusTrunc(img,num):

    img1=img;
    (x,y) = img1.shape
    for i in range(0,x):
           for j in range(0,y):
               if (img[i,j]< num):
                img1[i,j]=0; 
               else: 
                 img1[i,j] = img[i,j]-int(num);                 
    return img1

img_raw = cv2.imread('lenna.tif')
img1 = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
(x,y) = img1.shape; #get the shape of the image
rectangle = 255*np.ones((x, y), dtype="uint8")
#create a blank image

#select ROI function
roi = cv2.selectROI(img_raw)
rectangle[int(roi[1]):int(roi[1]+roi[3]),
int(roi[0]):int(roi[0]+roi[2])] = 0;

x = np.uint8(70)
img3 = minusTrunc(img1,x)  #darkened image 

logic = cv2.bitwise_or(rectangle,img3)   #select roi of darkened image

img_raw = cv2.imread('lenna.tif')
img1 = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)   #get new raw image
(x,y) = img1.shape; #get the shape of the image

img1[int(roi[1]):int(roi[1]+roi[3]),      #select roi in new raw image
int(roi[0]):int(roi[0]+roi[2])] = 255;

logic1 = cv2.bitwise_and(logic,img1)      #put together darkened and raw images

Hori = np.concatenate((img1,logic,logic1),axis=1)
cv2.imshow("rect operation",Hori)
cv2.imwrite("result.jpeg",logic1)

cv2.waitKey(0)
