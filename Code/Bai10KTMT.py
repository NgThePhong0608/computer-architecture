import cv2
import RPi.GPIO as GPIO
import time


def main():
    BT2 = 4
    BT3 = 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = "Camera User"
    capture = cv2.VideoCapture(0)
    print("Capture OK")
    fourcc = cv2.VideoWriter__fourcc(*'DIVX')
    out = cv2.VideoWriter(
        'output.avi', cv2.VideoWriter__fourcc(*'MJPG'), 20.0, (640, 480))
    cap_video = False
    while True:
        ret, frame = capture.read()
        if GPIO.input(BT2) == GPIO.LOW:
            print("Press BT2")
            cv2.imshow(namewindow, frame)
            out.write(frame)
            print("Video lưu")
            if cv2.waitkey(1) & 0xFF == ord('q'):
                GPIO.cleanup()
                cv2.destroyWindow(namewindow)
                break
            continue
        if GPIO.input(BT3) == GPIO.LOW:
            print("Press BT3")
            if cap_video:
                cap_video = False
                cv2.destroyWindow(namewindow)
                continue
            if not cap_video:
                cap_video = True
                continue
            time.sleep(0.5)
        if cap_video:
            cv2.imshow(namewindow, frame)
            out.write(frame)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            GPIO.cleanup()
            cv2.destroyWindow(namewindow)
            break


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyWindow(namewindow)
