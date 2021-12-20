# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
time.sleep(3)    
while True:
    # num = input("Enter a number: ") # Taking input from user
    # value = write_read(num)
    print(write_read("98")) # printing the value
    time.sleep(3)
    print(write_read("44")) # printing the value
    time.sleep(3)
    # print('9') # printing the value
    # print('8') # printing the value
    # print('.') # printing the value
    # stri = arduino.readline()
    # print(stri)