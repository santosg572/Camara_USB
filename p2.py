import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

print(type(cap))

def DespliegaImagen():
  while(True):
    ret, frame = cap.read()
    print(type(ret))
    print(type(frame))

    cv2.imshow('frame',frame)
    if cv2.waitKey(1):
        break
  return frame

fm = DespliegaImagen()
time.sleep(10)

cv2.imwrite('img.jpg', fm, [cv2.IMWRITE_JPEG_QUALITY, 100])
  
cap.release()
cv2.destroyAllWindows()

