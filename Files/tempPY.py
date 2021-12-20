import cv2
import serial
import time
arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# def detect_face():


time.sleep(3)
print(write_read("26"))
time.sleep(2)
# 26 to use sensor 1
# 980 to use sensor 2
error_manager = 5
video = cv2.VideoCapture(0)
# load "haarcascade_frontalface_default.xml" by creating a CascadeClassifier
# object as cascade
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
true_for_if = True
face_detected = False
print(write_read("98"))
while True:
    check, frame = video.read()

    # Image from webacm is in the format of BGR i.e combination of 3 colours
    # which will basicall require more amount of computation.
    # so we convert it into a gray scale image which is only single colour
    # and requires less computation.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Now we use detectMultiScale method to detect the faces in the video
    # stream. Which will return x,y,w,h which are basically the positions
    # with which we create a rectangle box.
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    # using for loop to go through the locations x,y,w,h and drow a rectangle
    for x, y, w, h in face:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)
        face_detected = True
    if not face_detected and true_for_if:
        print("no face detected")
        if not face_detected and true_for_if and error_manager <= 0:
            print(write_read("44"))
            time.sleep(1)
            true_for_if = False
            print(true_for_if)
        elif error_manager > 0:
            error_manager -= 1
            # time.sleep(0.2)
    elif face_detected and (not true_for_if):
        print("face detected")
        if face_detected and (not true_for_if) and error_manager >= 5:
            print(write_read("98"))
            time.sleep(1)
            true_for_if = True
            print(true_for_if)
        elif error_manager <= 5:
            error_manager += 1
    print(error_manager)
    cv2.imshow("Video", frame)
    face_detected = False
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
