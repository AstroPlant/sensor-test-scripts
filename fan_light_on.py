#! /usr/bin/python
 
import sys
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
CTRL_PIN = 21
GPIO.setup(CTRL_PIN, GPIO.OUT)
 
print ("FAN + Light CTRL Test (CTRL+C to exit)")
time.sleep(2)
print ("Ready")

try:

  print ("On")
  GPIO.output(CTRL_PIN, True)

except KeyboardInterrupt:
  print ('Quit')
  GPIO.cleanup()
except:
  print ('Unexpected error: ', sys.exc_info()[0])
