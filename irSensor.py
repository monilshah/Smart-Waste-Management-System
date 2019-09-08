import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

while True:
    sensor=GPIO.input(17)
    
    print(sensor)
    
    sleep(1)
        
GPIO.cleanup()