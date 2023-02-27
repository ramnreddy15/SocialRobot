import serial
import time

#declaring arduino PWM control device for drivetrain
ser = serial.Serial("/dev/ttyACM0", 9600)

#Control Loop to send PWM values continously to the arduino
while True:
    :


