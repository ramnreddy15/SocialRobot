import RPi.GPIO as GPIO
from time import sleep

try:
    GPIO.cleanup()
except:
    print("GPIO CALIBRATED")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18,100)

pwm.start(50)


i = 14.4


while i < 16:
    pwm.ChangeDutyCycle(i)
    sleep(0.1)
    print(i)
    i += 0.01
pwm.stop()


GPIO.cleanup()
