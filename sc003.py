import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



#----Declaration of ultrasonic sensor pins----
TRIG1=2
ECHO1=3
TRIG2=4
ECHO2=17
TRIG3=27
ECHO3=22 
TRIG5=18
ECHO5=23
TILT=24
#-------Ultrasonic sensor i/o--------
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(TRIG5,GPIO.OUT)
GPIO.setup(ECHO5,GPIO.IN)
GPIO.setup(TILT,GPIO.IN)

#----Get distance in cm from ultrasonic sensor----
def getcm(TRIG,ECHO):
    print("sending ping pin trig" + str(TRIG))
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
    
    return distance

#-----------tilt sensor-----------
falls = 0
n= 0
def outFunction(null):
    global n
    print("Singal detected " + str(n) + "\n")
    n = n+1
    
GPIO.add_event_detect(TILT, GPIO.FALLING, callback=outFunction, bouncetime = 100)







#--------MAIN LOOP--------------- 
while True:
    
    #---get distance for erach sensor
    distance1 = getcm(TRIG1,ECHO1)
    print('Distance 1: {} cm'.format(int(distance1)))
    
    
    #---- detect fall -----
    oldn = n
    time.sleep(10)
    actualn = n
    diff = actualn - oldn
    
    
    if(diff > 5):
        falls = falls + 1
        print("Fall detected: " + str(falls))
    
    
    
    with open ('/var/www/html/data1.csv','a') as datafile:
        
        datafile.write(str(falls) +  "\n")  
        
    with open ('/var/www/html/datau1.csv','a') as datafile:
        
        datafile.write(str(int(distance1)) +  "\n")      
 
    time.sleep(1)
 
GPIO.cleanup()
