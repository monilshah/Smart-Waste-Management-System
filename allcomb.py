import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 16
GPIO_ECHO = 18

LED_IN =22



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



def setAngle(angle):
    duty= angle/18+2
    GPIO.output(3,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(3,False)
    pwm.ChangeDutyCycle(0)
    
def callback(channel,num):
    
    type = -1
    time.sleep(2)
    
    if GPIO.input(channel):
        print (i+1,". No Water Detected!")
        type = 0
    else:
        print (i+1,". Water Detected!")
        type = 1
    return type


if __name__ == '__main__':
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_IN,GPIO.IN)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
    GPIO.setup(3,GPIO.OUT)
    pwm = GPIO.PWM(3,50)
    pwm.start(0)

    setAngle(90)
    
    channel = 38
    
    GPIO.setup(channel, GPIO.IN)
    
    passone = 0
    
    print("Pass 1")
    
    while True:
        sensor = GPIO.input(LED_IN)
        if sensor ==1:
            passone=1
            print("ir working")
            break
        
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    i=0
    
    time.sleep(5)
    
    passtwo=0
    
    print("Pass 2")
    
    if passone==1:
        type = callback(channel,i)
        passtwo=1
        
        if type==0:
            setAngle(180)
            time.sleep(2)
            setAngle(80)
        else:
            setAngle(0)
            time.sleep(2)
            setAngle(80)
    time.sleep(1)
     
    try:
        print("Pass 3")
        i=0
        while i<30:
           # print("Test1")
            dist = distance()
            #print("Test 2")
            print((i+1),". Measured Distance = %.lf cm" % dist)
            #print("Test 3")
            
            GPIO.setup(15, GPIO.OUT)
            GPIO.setup(13, GPIO.OUT)
            GPIO.setup(11, GPIO.OUT)
            
            if dist>=38:
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)
                
                #green
                
            elif dist>=17 and dist<38:
                GPIO.output(11, False)
                GPIO.output(15, False)
                GPIO.output(13, True)
                #yellow
            elif dist<17:
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, False)
                
                #red
                
            time.sleep(1)
            i=i+1
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
     
            
            
        
    pwm.stop()
    GPIO.cleanup()
    
   