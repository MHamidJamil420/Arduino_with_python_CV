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
print(write_read("26"))
time.sleep(2)
requiredDelay = 0.9
while True:
    # num = input("Enter a number: ") # Taking input from user
    # value = write_read(num)
    print(write_read("98"))  # printing the value
    time.sleep(requiredDelay)

    # print(write_read("23"))  # printing the value
    # time.sleep(requiredDelay)
    stri = arduino.readline()
    print(stri)

    print(write_read("44"))  # printing the value
    time.sleep(requiredDelay)

    # print(write_read("23"))  # printing the value
    # time.sleep(requiredDelay)
    stri = arduino.readline()
    print(stri)
