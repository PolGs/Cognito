import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
TRIG=21
ECHO=20
MOT=24
 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(MOT,GPIO.OUT)
 
while True:
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
 
 
    while GPIO.input(ECHO) == False:
        start = time.time()
 
    while GPIO.input(ECHO) == True:
        end = time.time()
 
    sig_time = end-start
 
    #cm:
    distance = sig_time / 0.000058 #inches: 0.0000148
 
 
    print('Distance:{} cm'.format(int(distance)))
    
    with open ('/var/www/html/data.csv','a') as datafile:
        
        datafile.write(str(int(distance)) + " \n")  
 
    time.sleep(1)
 
GPIO.cleanup()
