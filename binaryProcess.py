import numpy as np
import cv2
from autoCanny import *

def binaryProcess(image):

    # grayScale Image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # smooth to reduce noise a bit more
    blurred = cv2.GaussianBlur(gray, (5, 5),0)
    # Canny Process
    canny = auto_canny(blurred)
    return canny