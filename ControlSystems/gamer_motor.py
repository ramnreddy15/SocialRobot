import serial
import keyboard
import time

ser = serial.Serial("/dev/ttyACM0", 9600)

def activateMotor(val):
   ser.write(val.encode())


keyboard.on_press_key('w', lambda _:activateMotor("1530"))
keyboard.on_press_key('s', lambda _:activateMotor("1470"))
keyboard.on_release_key('w', lambda _:activateMotor("1500"))
keyboard.on_release_key('s', lambda _:activateMotor("1500"))



keyboard.wait('esc')

