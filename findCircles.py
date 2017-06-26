import numpy as np
import cv2
from sortContours import *
from drawNumbers import *
 
def findCircles(black_image,frame):
	circles = black_image
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
	lista = [] 
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	print "###########################################"
	print "Calculo das Distancias"
	print "###########################################"

	first = int(input("Informe o primeiro circulo: "))-1
	second = int(input("Informe o segundo circulo: "))-1
	print "lista = " +str(lista)
	print "Contours Size = " + str (len(cnts))
	(x1,y1),radius1 = cv2.minEnclosingCircle(cnts[first])
	(x2,y2),radius2 = cv2.minEnclosingCircle(cnts[second])
	p1 = (int(x1),int(y1))
	p2 = (int(x2),int(y2))
	cv2.line(frame,p1,p2,(0,0,255),5)
	cv2.imshow("Distancia", frame)
	cv2.waitKey(0)
   