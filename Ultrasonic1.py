import RPi.GPIO as GPIO
from picamera import PiCamera
import time

usleep = lambda x : time.sleep(x/1000000.0)

import datetime as dt

TP = 4

EP = 17

def getDistance():
	fdistance = 0.0
	nStartTime, nEndTime = 0,0
	GPIO.output(TP, GPIO.LOW)
	usleep(2)
	GPIO.output(TP, GPIO.HIGH)
	usleep(10)
	
	GPIO.output(TP, GPIO.LOW)


	while(GPIO.input(EP) == GPIO.LOW):
		pass
	nStartTime = dt.datetime.now()

	while(GPIO.input(EP) == GPIO.HIGH):
		pass
	nEndTime = dt.datetime.now()

	fDistance = (nEndTime - nStartTime).microseconds / 29. / 2.
	return fDistance

GPIO.setmode(GPIO.BCM)

GPIO.setup(TP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(EP, GPIO.IN)
time.sleep(0.5)

camera=PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15

usleep(5)
imageCount=0
timeCount=0
print("Start")
while(1):
	fDistance = getDistance()
	if fDistance <= 30:
		timeCount += 1
		print(str(timeCount))
		if timeCount >= 3:
			camera.capture("/home/haram/Project/refridge_raspberryPi/Images/image%d.jpg"%imageCount)
			print(str(fDistance)+", Captured")
			imageCount += 1
			timeCount = 0
	else:
		timeCount = 0
	time.sleep(1)

