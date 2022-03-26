import cv2 
import RPi.GPIO as GPIO
import time

def main():
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = "Camera User"
    capture = cv2.VideoCapture(0)
    print("Capture OK")
    while True:
        ret, frame = capture.read()
        if GPIO.input(BT1) == GPIO.LOW:
            while True:
                cv2.imshow("Ảnh chụp camera: ", frame)
                cv2.waitkey()
                cv2.destroyWindow()
                break
try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyWindow(namewindow)