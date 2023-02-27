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


d = 10.0
while True:
    print(d)
    pwm.ChangeDutyCycle(d);
    d+=1.0
    sleep(0.5)
GPIO.cleanup()
