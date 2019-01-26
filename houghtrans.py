import cv2
import numpy as np

im = cv2.imread('rec4.jpg',0)

scale_percent = 25 # percent of original size
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
imS=cv2.resize(im,dim, interpolation = cv2.INTER_AREA)

cimg = cv2.cvtColor(imS,cv2.COLOR_GRAY2BGR)

rows = imS.shape[0]

circles = cv2.HoughCircles(imS,cv2.HOUGH_GRADIENT,1,rows/28,param1=230,param2=30,minRadius=10,maxRadius=30)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),4)

cv2.imshow("output",cimg)
cv2.imshow("Input", imS)  
cv2.waitKey(0)
cv2.destroyAllWindows()

