import RPi.GPIO as GPIO
from time import sleep

def setAngle(angle):
    duty= angle/18+2
    GPIO.output(3,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)



GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
pwm = GPIO.PWM(3,50)
pwm.start(0)

setAngle(90)

type = 1 #type0=wet;type1=dry

if type==0:
    setAngle(180)
    sleep(2)
    setAngle(0)
else:
    setAngle(0)
    sleep(2)
    setAngle(180)

pwm.stop()
GPIO.cleanup()