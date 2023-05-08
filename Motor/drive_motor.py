import serial
import time 

#declaring arduino PWM control device for drivetrain
ser = serial.Serial("/dev/ttyACM0", 9600)

currState = 1500
ser.write("1500".encode())
#Control Loop to send PWM values continously to the arduino
while True:
    input_value = input("Enter direction (w, a, d, k): ")
    
    if(input_value == "k"):
        ser.write("1500 1500".encode())

    if(input_value == "d"):
        ser.write("1540 1500".encode())

    if(input_value == "a"):
        ser.write("1500 1540".encode())

    if(input_value == "w"):
        ser.write("1540 1540".encode())

