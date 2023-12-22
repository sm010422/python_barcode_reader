import cv2
from pyzbar.pyzbar import decode


# capture webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    frame = cv2.flip(frame, 1)
    cv2.imshow('scanner', frame)
    if cv2.waitKey(1) == ord('q'):
        break
