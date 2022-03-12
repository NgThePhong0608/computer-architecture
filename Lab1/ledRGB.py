import RPi.GPIO as GPIO
import time
import os


def main():
    LED_R = 17
    LED_G = 18
    LED_B = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    while True:
        # red
        if GPIO.input(LED_R) == GPIO.LOW:
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.HIGH)
            GPIO.output(LED_B, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(LED_R) == GPIO.HIGH:
            GPIO.output(LED_R, GPIO.LOW)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_B, GPIO.HIGH)
            time.sleep(0.5)
        # green
        # if GPIO.input(LED_G) == GPIO.LOW:
        #     GPIO.output(LED_G, GPIO.HIGH)
        #     time.sleep(0.5)
        # if GPIO.input(LED_G) == GPIO.HIGH:
        #     GPIO.output(LED_G, GPIO.LOW)
        #     time.sleep(0.5)
        # # blue
        # if GPIO.input(LED_B) == GPIO.LOW:
        #     GPIO.output(LED_B, GPIO.HIGH)
        #     time.sleep(0.5)
        # if GPIO.input(LED_B) == GPIO.HIGH:
        #     GPIO.output(LED_B, GPIO.LOW)
        #     time.sleep(0.5)


while 1:
    main()
    pass
