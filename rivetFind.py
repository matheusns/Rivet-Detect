import cv2
import numpy as np
from autoCanny import *
# from binaryProcess import *
#Video Capture
cap = cv2.VideoCapture(1)
while(True):
    # Frame Capture
    ret, frame = cap.read()
    # Black Image
    black_image = np.zeros((cap.get(4),cap.get(3),1),np.uint8)
    # grayScale Image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # smooth to reduce noise a bit more
    blurred = cv2.GaussianBlur(gray, (5, 5),0)
    # Thresholding 
    ret3,threshold = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    canny = auto_canny(threshold)
    cimg = frame.copy()
    # Circles Detect  
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 0.1, 200, np.array([]), 120, 30, 1, 30)    
    # ensure at least some circles were found
    if circles is not None:
        print ""
        print "Tamanho de Circle = " + str(circles)
        c = np.uint16(np.around(circles))
        #a, b, c = circles.shape
        for i in c[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            #im2, contours, hierarchy = cv2.findContours(black_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # print "Tamanho da lista = " + str(len(contours))
            #cnt = contours[0]
            #cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
            #area = cv2.contourArea(cnt)
            #equi_diameter = np.sqrt(4*area/np.pi)
           # print "Diametro = " + str(equi_diameter)            
            cv2.imshow("Threshold", canny)
            #cv2.imshow("black_image", black_image)
            cv2.imshow("Circles Detected", cimg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        print "Acabou!"