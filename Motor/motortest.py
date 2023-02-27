from gpiozero import Servo, Device
from time import sleep
from gpiozero.pins.native import NativeFactory
Device.pin_factory = NativeFactory()
servo = Servo(17)

GPIO.cleanup()

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
