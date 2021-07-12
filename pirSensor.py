import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensorPin = 16
bluePin = 20
redPin = 21

GPIO.setup(sensorPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

try:
    while(1):
        if GPIO.input(sensorPin) == GPIO.LOW:
            print('motion detected')
            GPIO.output(bluePin, GPIO.HIGH)
            GPIO.output(redPin, GPIO.LOW)
        else:
            print('No motion')
            GPIO.output(bluePin, GPIO.LOW)
            GPIO.output(redPin, GPIO.HIGH)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    exit(0)
