# camera_bai13_2
import cv2
import copy
from config import Config
import RPi.GPIO as GPIO


def main():
    BT1 = 14
    BT2 = 4
    # open camera
    cap = cv2.VideoCapture(-1)
    print('Cap oke!')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    isdraw = False

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print('BT1 is pressed!')
            while True:
                ret, src = cap.read()
                frame = copy.copy(src)
                hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
                green_mark = cv2.inRange(hsv, (35, 89, 107), (45, 241, 213))
                _, contoursGreen, _ = cv2.findContours(
                    green_mark, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                red_mark = cv2.inRange(hsv, (0, 118, 130), (5, 255, 255))
                _, contoursRed, _ = cv2.findContours(
                    red_mark, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                group = green_mark + red_mark
                group = group >= 1

                group = group.astype("uint8") * 255
                result = cv2.bitwise_or(frame, frame, mask=group)

                if GPIO.input(BT2) == GPIO.LOW:
                    isdraw = True
                if isdraw:
                    draw(contoursGreen, contoursRed, result)
                cv2.imshow('Camera', src)
                cv2.imshow('Threshould', result)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    GPIO.cleanup()
                    cv2.destroyAllWindows()
                    break


def nothing(x):
    pass


def draw(contoursGreen, contoursRed, frame):
    for i in range(len(contoursRed)):
        if cv2.contourArea(contoursRed[i]) > 300:
            hull = cv2.convexHull(contoursRed[i])
            cv2.drawContours(frame, [hull], -1, (0, 0, 255))
    for i in range(len(contoursGreen)):
        if cv2.contourArea(contoursGreen[i]) > 300:
            hull = cv2.convexHull(contoursGreen[i])
            cv2.drawContours(frame, [hull], -1, (0, 255, 0))


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyAllWindows()
