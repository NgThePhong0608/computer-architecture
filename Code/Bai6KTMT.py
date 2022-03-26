import RPi.GPIO as GPIO
from config import Config
import time


def main():
    BT1 = 14
    BT2 = 4
    BT3 = 3
    BT4 = 2
    DIR = 19
    PWD = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(PWD, GPIO.OUT)
    global PWD1, PWD2
    PWD1 = GPIO.PWM(DIR, 100)
    PWD2 = GPIO.PWM(PWD, 100)
    PWD1.start(0)
    PWD2.start(0)
    currentPWD1 = 20
    currentPWD2 = 20
    print("Chuẩn bị hoàn tất ok")
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print('BT1 press')
            PWD2.ChangeDutyCycle(0)
            time.sleep(1)
            upPWD = 20
            currentPWD1 = (currentPWD1 + upPWD) if currentPWD1 < 100 else 100
            handleDutyCycle(PWD1, currentPWD1, currentPWD2)
            print('Tốc độ hiện tại: ' + str(currentPWD1) + 'theo chiều thuận')
            currentPWD2 = 0
            time.sleep(0.5)
        if GPIO.input(BT2) == GPIO.LOW:
            print('BT2 press')
            PWD2.ChangeDutyCycle(0)
            downPWD = 20
            currentPWD1 = (currentPWD1 - downPWD) if currentPWD1 > 0 else 0
            handleDutyCycle(PWD1, currentPWD1, currentPWD2)
            currentPWD2 = 0
            time.sleep(0.5)
        if GPIO.input(BT3) == GPIO.LOW:
            print('BT3 press')
            PWD1.ChangeDutyCycle(0)
            upPWD = 20
            currentPWD2 = (currentPWD2 + upPWD) if currentPWD2 < 100 else 100
            handleDutyCycle(PWD2, currentPWD2, currentPWD1)
            print("Tốc độ hiện tại: " + '-' + str(currentPWD2))
            currentPWD1 = 0
            time.sleep(0.5)
        if GPIO.input(BT4) == GPIO.LOW:
            print('BT4 press')
            PWD1.ChangeDutyCycle(0)
            downPWD = 20
            currentPWD2 = (currentPWD2 - downPWD) if currentPWD2 > 0 else 0
            print("Tốc độ hiện tại: " + '-' + str(currentPWD2))
            handleDutyCycle(PWD2, currentPWD2, currentPWD1)
            currentPWD1 = 0
            time.sleep(0.5)


def handleDutyCycle(PWD, currentPWD, currentPWDpre):
    print(currentPWDpre)
    if currentPWD > 100 or currentPWD < 0:
        print('Không thể tăng hay giảm tốc được nữa')
        return
    elif currentPWDpre != 0:
        time.sleep(1)
    PWD.ChangeDutyCycle(currentPWD)


try:
    main()
except KeyboardInterrupt:
    PWD1.stop()
    PWD2.stop()
    GPIO.cleanup()
