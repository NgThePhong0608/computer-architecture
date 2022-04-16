# camera_bai13
import cv2
import RPi.GPIO as GPIO
import numpy as np
import copy


def main():
    BT1 = 14
    BT2 = 4
    # open camera
    cap = cv2.VideoCapture(0)
    print('Cap oke!')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    isdraw = False

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print("BT1 is pressed!")
            while True:
                ret, src = cap.read()
                frame = copy.copy(src)
                hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
                mark = cv2.inRange(hsv, (0, 118, 130), (0, 255, 255))
                _, contours, _ = cv2.findContours(
                    mark, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                result = cv2.bitwise_or(frame, frame, mask=mark)

                if GPIO.input(BT2) == GPIO.LOW:
                    print("BT2 is pressed!")
                    isdraw = True
                if isdraw:
                    draw(contours, result)
                cv2.imshow('Camera', src)
                cv2.imshow('Threshould', result)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    GPIO.cleanup()
                    cv2.destroyAllWindows()
                    break


def nothing(x):
    pass


def draw(contours, frame):
    if contours is None:
        print("No contours. Try again!")
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 300:
            hull = cv2.convexHull(contours[i])
            cv2.drawContours(frame, [hull], -1, (0, 0, 255))


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyAllWindows()
