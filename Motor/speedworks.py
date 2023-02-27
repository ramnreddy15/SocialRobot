import RPi.GPIO as GPIO
from time import sleep

try:
    GPIO.cleanup()
except:
    print("GPIO CALIBRATED")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 100)

pwm.start(50)

#pwm.ChangeDutyCycle(17)
#sleep(1)

for i in range(10,17):
    print(i)
    pwm.ChangeDutyCycle(i)
    sleep(2)
    
pwm.stop()

GPIO.cleanup()
