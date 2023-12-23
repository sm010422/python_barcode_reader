import cv2
from pyzbar.pyzbar import decode
#from pydub import AudioSegment 
#from pydub.playback import play 


# capture webcam
cap = cv2.VideoCapture(1)

#song =  AudioSegment.from_wav("Barcode-scanner-beep-sound.wav")
while cap.isOpened():
    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    detectedBarcode = decode(frame)
    if not detectedBarcode:
        print("No Barcode")
    else:
        for barcode in detectedBarcode:
            if barcode.data != "":
                cv2.putText(frame,str(barcode.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                #play(song)
                cv2.imwrite("code.png",frame)
                

    cv2.imshow('scanner', frame)
    if cv2.waitKey(1) == ord('q'):
        break

