import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라　기본　
# 영상　캡쳐，　녹화　
cap = cv2.VideoCapture(0) #번호　０번부터　웹캠　열기　
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

font = ImageFont.truetype('/usr/share/fonts/nanumfont/NanumGothic.ttf', 20)

#loop (while input 'q')
while True:
    ret, frame = cap.read()
    h, _, _ = frame.shape
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') # 20210720_164725
    if ret != True: break

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)

    draw.text(xy=(20, h-40), text='REC - {0}'.format(currDateTime), font=font, fill=(0,0,255))
    frame = np.array(frame)

    # cv2.imshow('Gray Color CAM', gray)
    cv2.imshow('RealTime CAM', frame)
    key = cv2.waitKey(1)
    if key == ord('q'): break #종료
    elif key == ord('c'): #캡쳐
        cv2.imwrite('./capture/img_{}.png'.format(fileDateTime), frame)
        print('이미지　캡쳐　성공')
    
    

cap.release() # 웹캠　인스턴스　해제　
cv2.destroyAllWindows()
