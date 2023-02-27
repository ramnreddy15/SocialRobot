import serial
import keyboard
import time

ser = serial.Serial("/dev/ttyACM0", 9600)

ser.write("1500".encode())

def activateMotor(val):
   ser.write(val.encode())


keyboard.on_press_key('w', lambda _:activateMotor("1540 1540"))

keyboard.on_press_key('s', lambda _:activateMotor("1430 1430"))

keyboard.on_press_key('d', lambda _:activateMotor("1540 1500"))

keyboard.on_press_key('a', lambda _:activateMotor("1500 1540"))

keyboard.on_release_key('w', lambda _:activateMotor("1500 1500"))

keyboard.on_release_key('s', lambda _:activateMotor("1500 1500"))

keyboard.on_release_key('d', lambda _:activateMotor("1500 1500"))

keyboard.on_release_key('a', lambda _:activateMotor("1500 1500"))

keyboard.wait('esc')

