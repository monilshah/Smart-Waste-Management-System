import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 

    try:
        count =0
        print(1)
        while count<5:
            print(2)
            dist = distance()
            print(3)
            print((count+1),". Measured Distance = %.lf cm" % dist)
            print(4)
            if dist>=22.5 and dist<30:
                GPIO.setup(37, GPIO.OUT)
                GPIO.output(37, True)
                
                #green
                
            elif dist>=15 and dist<22.5:
                GPIO.setup(33, GPIO.OUT)
                GPIO.output(33, True)
                #yellow
            elif dist<15:
                GPIO.setup(31, GPIO.OUT)
                GPIO.output(31, True)
                #red
            
            
            count = count +1
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
GPIO.cleanup()
