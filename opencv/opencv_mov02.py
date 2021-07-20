import cv2
import numpy as np

cap = cv2.VideoCapture(0) #번호　０번부터　웹캠　열기　
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#loop (while input 'q')
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret != True: break
    
    cv2.imshow('Gray Color CAM', gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # 웹캠　인스턴스　해제　
cv2.destroyAllWindows()
