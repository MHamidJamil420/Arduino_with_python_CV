import cv2
import pickle
import time
import serial
port = serial.Serial('COM10', 9600)

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    og_label = pickle.load(f)
    labels = {v: k for k, v in og_label.items()}
    print(labels)


sampleno = 0
conditional_status = False
data_to_be_send = 1
prev_data = 1
temp_str = ""
glob_str = ""
port.write(str.encode("26"))
time.sleep(2)
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    # print(face)

    for x, y, w, h in face:
        face_save = gray[y:y+h, x:x+w]

        ID, conf = recognise.predict(face_save)
        # print(ID,conf)
        if conf >= 25 and conf <= 115:
            print(ID)
            print(labels[ID])
            cv2.putText(frame, labels[ID], (x-10, y-10),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)

            # if(ID == 0):
            if not (str(ID+1) in temp_str):
                temp_str += str(ID+1)
            #     data_to_be_send *= 10
            #     data_to_be_send += (ID+1)
            # if(ID == 1):
            #     data_to_be_send *= 10
            #     data_to_be_send += (ID+1)
            # if(ID == 2):
            #     data_to_be_send *= 10
            #     data_to_be_send += (ID+1)
            # if data_to_be_send == 1:
            #     data_to_be_send = 22
            #     print("unknown face detected")
            # if not (prev_data == data_to_be_send):
            #     print("New Data : ", str(data_to_be_send))
            #     prev_data = data_to_be_send
            # data_to_be_send = 1
            # we have to send prev_data to arduino
            # print("we got ID : ",ID)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 4)
    data_to_be_send = 1
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

    if not (glob_str == temp_str):
        glob_str = temp_str
        temp_str.replace(" ", "")
        print("Sending : ", temp_str)
        port.write(str.encode((temp_str+"1")))
        time.sleep(1.5)
        # {----}
        # time.sleep(.5)
    elif temp_str == "":
        print("No image detected!")
        print("Sending 11")
        port.write(str.encode("11"))
        time.sleep(1)
        # {----}
    temp_str = ""
    time.sleep(.3)

    print("new itreration")

video.release()
cv2.destroyAllWindows()
