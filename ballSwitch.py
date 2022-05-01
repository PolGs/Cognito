import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN)

print ("Sensor-test [press ctrl+c to end]")

n= 0

def outFunction(null):
    global n
    print("Singal detected " + str(n) + "\n")
    n = n+1
    
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime = 100)


try:
    while True:
        time.sleep(1)
        
        
except KeyboardInterrupt:
    GPIO.CLEANUP()
    