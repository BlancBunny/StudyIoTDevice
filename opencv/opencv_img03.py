# crop (자르기)

import cv2
import numpy as np

original = cv2.imread('./image/python.png', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

h,w,c = original.shape
cropped = gray[:, :int(w/2)] # 이미지　가로　반으로　자르기
# cropped = gray[:int(h/2), :] # 이미지　세로　반으로　자르기

cv2.imshow('original', original) # cv2 새 윈도우창 생성
cv2.imshow('cropped', cropped)

cv2.waitKey(0) # 키입력 대기(ESC)
cv2.destroyAllWindows() # 메모리 해제 
