import cv2 

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID 비디오　선택
is_record = False

while True:
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Origin Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지　캡쳐　완료')
        elif key == ord('r') and is_record == False: # r　입력시　녹화　시작
            is_record = True
            video = cv2.VideoWriter('./capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
            print('동영상　촬영　시작')
        elif key == ord('r') and is_record == True: # 녹화중일때
            is_record = False
            video.release()
            print('동영상　촬영　끝')

        if is_record:
            video.write(frame)

cam.release()
cv2.destroyAllWindows()

