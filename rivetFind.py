import cv2
import numpy as np
from binaryProcess import *
from findCircles import *

#Video Capture
cap = cv2.VideoCapture(0)
fn = "black.jpg"
cont = 0
while True:
    ret, frame = cap.read()
    cv2.imshow("Checking the frame position",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
while(cont!=100):
    # print "Cont = " + str(cont)
    # Frame Capture
    ret, frame = cap.read()
    if cont==0:
        # Black Image
        black_image = np.zeros((cap.get(4),cap.get(3),1),np.uint8)
    binary = binaryProcess(frame)
    # Circles Detect  
    circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 0.1, 200, np.array([]), 50, 30, 1, 30)    
    # ensure at least some circles were found
    if circles is not None:
        c = np.uint16(np.around(circles))
        for i in c[0,:]:
            # draw the circles
            # print "Raio = " + str(i[2])
            # if i[2]>=17:
            cv2.circle(black_image,(i[0],i[1]),5,(255,255,255),12,) #Drawing the circle
            cv2.imshow("black_image", black_image)
            cv2.imshow("Canny", binary)
            cv2.imshow("BRG", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
   
    cont+=1

# cv2.destroyAllWindows()
findCircles(black_image,frame)