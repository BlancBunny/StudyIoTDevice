from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
    print('picture : %s' % i)
    sleep(1)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()

