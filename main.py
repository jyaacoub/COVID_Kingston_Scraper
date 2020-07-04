from scraper import Bot

# bot = Bot()
# bot.requestContent()
# print("Active Cases:", bot.getCases())
# print("Community Status:", bot.getCommunityStatus())
from gpiozero import PWMLED
from time import sleep

red = PWMLED(5)
green = PWMLED(6)
blue = PWMLED(13)


def displayColor(color='w'):

    if color == 'w':
        red.on()
        green.on()
        blue.on()
    elif color == 'r':
        red.on()
        green.off()
        blue.off()
    elif color == 'o':
        green.value = 0.05
        red.value = 1.0

        blue.off()
    elif color == 'y':
        green.value = 0.25
        red.value = 1.0

        blue.off()
    elif color == 'g':
        red.off()
        green.on()
        blue.off()

# Sub in 2 for Red, 3-Orange, 4-Yellow, and 5-Green
#while True:
    # Red
   # displayColor('r')
   # sleep(1)

    # Orange
   # displayColor('o')
   # sleep(1)

    # Yellow
   # displayColor('y')
   # sleep(1)

    # Green
   # displayColor('g')
   # sleep(1)

# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO ports for the 7seg pins
segments = (11, 4, 23, 8, 7, 10, 18, 25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# GPIO ports for the digit 0-3 pins
digits = (22, 27, 17, 24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)

# num = {' ': (0, 0, 0, 0, 0, 0, 0),
#        '0': (1, 1, 1, 1, 1, 1, 0),
#        '1': (0, 1, 1, 0, 0, 0, 0),
#        '2': (1, 1, 0, 1, 1, 0, 1),
#        '3': (1, 1, 1, 1, 0, 0, 1),
#        '4': (0, 1, 1, 0, 0, 1, 1),
#        '5': (1, 0, 1, 1, 0, 1, 1),
#        '6': (1, 0, 1, 1, 1, 1, 1),
#        '7': (1, 1, 1, 0, 0, 0, 0),
#        '8': (1, 1, 1, 1, 1, 1, 1),
#        '9': (1, 1, 1, 1, 0, 1, 1)}
#
# try:
#     while True:
#         n = time.ctime()[11:13] + time.ctime()[14:16]
#         s = str(n).rjust(4)
#         for digit in range(4):
#             for loop in range(0, 7):
#                 GPIO.output(segments[loop], num[s[digit]][loop])
#                 if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
#                     GPIO.output(25, 1)
#                 else:
#                     GPIO.output(25, 0)
#             GPIO.output(digits[digit], 0)
#             time.sleep(1)
#             GPIO.output(digits[digit], 1)
# finally:
#     GPIO.cleanup()

