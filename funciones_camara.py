import numpy as np
import cv2
import time

def CapturaImg(file=''):
  cap = cv2.VideoCapture(0)

  def DespliegaImagen():
    while(True):
      ret, frame = cap.read()

#      cv2.imshow('frame',frame)
      if cv2.waitKey(1):
          break
    return frame

  fm = DespliegaImagen()
  time.sleep(10)

  cv2.imwrite(file+'.jpg', fm, [cv2.IMWRITE_JPEG_QUALITY, 100])
  
  cap.release()
  cv2.destroyAllWindows()

