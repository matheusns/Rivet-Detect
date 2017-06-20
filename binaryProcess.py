import numpy as np
import cv2

def binaryProcess(image):

    # grayScale Image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # smooth to reduce noise a bit more
    blurred = cv2.GaussianBlur(gray, (5, 5),0)
    # Thresholding 
    ret3,threshold = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return threshold