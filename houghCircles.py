import cv2
import numpy as np

from autoCanny import *

#Video Capture
cap = cv2.VideoCapture(0)

while(True):
    #Frame Capture
    ret, frame = cap.read()
    #Black Image
    black_image = np.zeros((cap.get(4),cap.get(3),1),np.uint8)
    #grayScale Image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #smooth to reduce noise a bit more
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # bi = cv2.bilateralFilter(gray,9,75,75)
    
    # Edge Processing 
    # edgeImage = auto_canny(blurred)
    
    #edgebi = auto_canny(bi)
    

    ###Circles Detect
    ##circles = cv2.HoughCircles (blurred,cv2.HOUGH_GRADIENT,1.2,30,40,150)
    ###Circles analize
    ##if circles is not None : 
	##    circles = np.round(circles[0,:]).astype("int") 
	##    for(x, y,r) in circles:
    ##         cv2.circle (black_image,(x,y),r,(0,255,0),4) 
    ##         cv2.rectangle (black_image,(x-5,y-5),(x+5,y+5),(0,128,255),- 1) 
    ##else:
    ##    print "Any circle detect"

    img = cv2.medianBlur(blurred, 5)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
    if circles is not None :   
        a, b, c = circles.shape
        for i in range(b):
            cv2.circle(black_image, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (255, 255, 255), 3, cv2.LINE_AA)
            cv2.circle(black_image, (circles[0][i][0], circles[0][i][1]), 2, (255, 255, 255), 3, cv2.LINE_AA) # draw center of circle
        
        cv2.imshow("source", frame)
        cv2.imshow("detected circles", black_image)
        ##cv2.imshow('Gauss', blurred)
        ##cv2.imshow('BGR', frame)
        ##cv2.imshow('Gray', gray)
        ##cv2.imshow('Edge', edgeImage)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
