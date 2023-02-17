from pynput import keyboard 
import time
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

def on_press(key):
    try:
        print(str(key), "Pressed")
        if("'w'" == str(key)):
            ser.write("1530".encode())
        if("'s'" == str(key)):
            ser.write("1500".encode())
            ser.write("1440".encode())
    except AtrributeError:
        print("special key {0} pressed".format(key))

def on_release(key):
    ser.write("1500".encode())
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

i=0
while(True):
    i+=1
    i-=1
