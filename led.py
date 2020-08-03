import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red = 21
green = 20
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0)

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(blue, 0)

try:
    while(True):
        req = raw_input("RGB: ")

        if (len(req) == 3):
            GPIO.output(red, int(req[0]))
            GPIO.output(green, int(req[1]))
            GPIO.output(blue, int(req[2]))
except KeyboardInterrupt:
    GPIO.cleanup()
