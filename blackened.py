import cv2
import numpy as np

img_raw = cv2.imread('lenna.tif')
img1 = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
(x,y) = img1.shape; #get the shape of the image
rectangle = 255*np.ones((x, y), dtype="uint8")
#create a blank image

#select ROI function
roi = cv2.selectROI(img_raw)
rectangle[int(roi[1]):int(roi[1]+roi[3]),
int(roi[0]):int(roi[0]+roi[2])] = 0;
logic = cv2.bitwise_and(rectangle,img1)

Hori = np.concatenate((rectangle,logic),axis=1)
cv2.imshow("rect operation",Hori)
cv2.imwrite("result.jpeg",logic)

cv2.waitKey(0)
