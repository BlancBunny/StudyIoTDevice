# 저장된　이미지　출력

import cv2
import numpy as np

original = cv2.imread('./image/python.png')

cv2.imshow('original', original) # cv2 새 윈도우창 생성

cv2.waitKey(0) # 키입력 대기(ESC)
cv2.destroyAllWindows() # 메모리 해제 
