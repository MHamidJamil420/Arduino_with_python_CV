import cv2

cap = cv2.VideoCapture(1)

while True:
    success, img = cap. read()
    cv2. imshow(" Image" ,img)
    cv2. waitKey(1)