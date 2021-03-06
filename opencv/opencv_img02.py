# resize (크기　조절)

import cv2
import numpy as np

original = cv2.imread('./image/python.png', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

h,w,c = original.shape
print('width : {0}, height : {1}, Channel : {2}'.format(w,h,c))
size_small = cv2.resize(gray, dsize=(int(w/2), int(h/2)))

cv2.imshow('original', original) # cv2 새 윈도우창 생성
cv2.imshow('gray', gray)
cv2.imshow('resize', size_small)

cv2.waitKey(0) # 키입력 대기(ESC)
cv2.destroyAllWindows() # 메모리 해제 
