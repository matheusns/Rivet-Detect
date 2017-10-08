import numpy as np
import cv2
import math as math
    
def distance(frame,cnts):
    backup = frame
    while (True):
        cont1 = 1
        todos = False
        framecp = np.zeros((640,480,1),np.uint8)
        framecp = backup.copy()
        print "Contours lenght = " + str(len(cnts))
        print "###########################################"
        print "Calculo das Distancias"
        print "###########################################" 
        first = int(input("Informe o primeiro circulo, zero para todas as distancias: "))
        if first == 0:
            todos = True
        else:
            second = int(input("Informe o segundo circulo: "))-1
        if todos == True:
            # print "Contours Size = " + str (len(cnts))
            for i in range(0,len(cnts)):
                cont1 = 1
                while cont1<len(cnts):
                    (x1,y1),radius1 = cv2.minEnclosingCircle(cnts[i])
                    (x2,y2),radius2 = cv2.minEnclosingCircle(cnts[cont1])
                    p1 = (int(x1),int(y1))
                    p2 = (int(x2),int(y2))            
                    cv2.line(framecp,p1,p2,(0,0,255),5)                    
                    cont1+=1
        else:
            # print "Contours Size = " + str (len(cnts))
            (x1,y1),radius1 = cv2.minEnclosingCircle(cnts[first-1])
            (x2,y2),radius2 = cv2.minEnclosingCircle(cnts[second])
            dist = math.hypot(int(x2) - int(x1), int(y2) - int(y1))
            p1 = (int(x1),int(y1))
            p2 = (int(x2),int(y2))
            cv2.line(framecp,p1,p2,(0,0,255),5)
            cv2.putText(framecp,"Dist = "+str(round(dist/60))+" cm",(300,450), cv2.FONT_HERSHEY_TRIPLEX, 1,(0,0,0),2)
            
        cv2.imshow("Distancia", framecp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print "Deseja Mais alguma distancia? 1 - Sim || 0 - Nao"
        saida = int(input())
        if (saida == 0):
            break
