import cv2
import copy
import RPi.GPIO as GPIO
from config import Config


def nothing(x):
    pass


def main():
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    cap = cv2.VideoCapture(0)
    print("Capture OK")
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print("Pres BT1")
            cv2.namedWindow('image')
            cv2.createTrackbar('lowH', 'image', 0, 180, nothing)
            cv2.createTrackbar('highH', 'image', 179, 180, nothing)
            cv2.createTrackbar('lowS', 'image', 0, 255, nothing)
            cv2.createTrackbar('highS', 'image', 255, 255, nothing)
            cv2.createTrackbar('lowV', 'image', 0, 255, nothing)
            cv2.createTrackbar('highV', 'image', 255, 255, nothing)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            while True:
                pass
