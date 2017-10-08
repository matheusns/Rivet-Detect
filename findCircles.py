import numpy as np
import cv2
from sortContours import *
from drawNumbers import *
from distance import *
 
def findCircles(black_image,frame):
	circles = black_image
	cimg = frame.copy()
	im2, cnts, hierarchy = cv2.findContours(circles,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# cv2.drawContours(frame, contours, -1, (0,255,0), 5)
	(cnts, boundingBoxes) = sort_contours(cnts)
	for (i, c) in enumerate(cnts):
		draw_contour(frame, c, i)
	for cnt in cnts:
	    (x,y),radius = cv2.minEnclosingCircle(cnt)
	    center = (int(x),int(y))
	    radius = int(radius)
	    cv2.circle(frame,center,50,(0,255,0),3)
	cv2.putText(frame,str(len(cnts)),(10,450), cv2.FONT_HERSHEY_TRIPLEX, 3,(255,255,255),4)
	cv2.imshow("Circles", frame)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	distance(frame,cnts)	