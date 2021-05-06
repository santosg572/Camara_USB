import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & time.sleep(10):
        break

cap.release()
cv2.destroyAllWindows()

