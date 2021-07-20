import cv2 

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Origin Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()

