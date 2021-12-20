from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("COM3")

while True:
    arduino.sendData([1])
    sleep(3)
    arduino.sendData([0])
    sleep(1)
