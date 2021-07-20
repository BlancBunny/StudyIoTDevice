import cv2
import numpy

img = cv2.imread('./image/python.png')
dst = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)



cv2.imshow('origin', dst)

cv2.waitKey(0)
cv2.destroyAllWindows() # instance quit
