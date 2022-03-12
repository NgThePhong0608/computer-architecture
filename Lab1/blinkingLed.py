import RPi.GPIO as GPIO
import time
import os


def main():
    LED = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)
    while True:
        if GPIO.input(LED) == GPIO.LOW:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)
        if GPIO.input(LED) == GPIO.HIGH:
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)


while 1:
    main()
    pass
