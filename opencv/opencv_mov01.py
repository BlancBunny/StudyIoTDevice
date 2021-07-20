import cv2
import numpy as np

cap = cv2.VideoCapture(0) #번호　０번부터　웹캠　열기　
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#loop (while input 'q')
while True:
    ret, frame = cap.read()

    if ret != True: break
    
    cv2.imshow('RealTime CAM', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # 웹캠　인스턴스　해제　
cv2.destroyAllWindows()
