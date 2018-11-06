from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()

now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d-%H")
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image'+now_str+'.jpg')
camera.stop_preview()