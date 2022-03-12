# import RPi.GPIO as GPIO
# import time
# import pio
# import Ports


# def peripheral_setup():
#     pio.terminal = Ports.SerialTerminal(9600)


# def main():
#     i = 0
#     BT1 = 4
#     LED = 22
#     GPIO.setmode(GPIO.BCM)
#     peripheral_setup()
#     GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(LED, GPIO.OUT)  # đặt đèn led output
#     while True:
#         if GPIO.input(BT1) == GPIO.LOW:
#             pio.terminal.print('Den bat')
#             GPIO.output(LED, GPIO.HIGH)
#             time.sleep(0.5)
#         else:
#             pio.terminal.print('Den tat')
#             GPIO.output(LED, GPIO.LOW)
#             time.sleep(0.5)


# if __name__ == '__main__':
#     main()
#     pass

import RPi.GPIO as GPIO
import time
import pio
import Ports


def peripheral_setup():
    pio.terminal = Ports.SerialTerminal(9600)


def main():
    BT1 = 4
    LED = 22
    GPIO.setmode(GPIO.BCM)
    peripheral_setup()
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)  # đặt đèn led output
    i = 0
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            pio.terminal.print('Ban bat cong tac: ')
            i = i + 1
            pio.terminal.println(str(i))
            time.sleep(0.5)
            if i == 1:
                GPIO.output(LED, GPIO.HIGH)
            if i == 2:
                GPIO.output(LED, GPIO.LOW)
                i = 0
