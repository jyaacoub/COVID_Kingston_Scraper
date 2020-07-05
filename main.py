from scraper import Bot
from gpiozero import PWMLED
import time

red = PWMLED(5)
green = PWMLED(6)
blue = PWMLED(13)


def getData():
    bot = Bot()
    bot.requestContent()
    communityStatus = bot.getCommunityStatus()
    activeCases = bot.getCases()
    print("Community Status:|" + communityStatus + '|')
    print("Active Cases:", activeCases)
    bot.quit()
    return communityStatus, activeCases


def displayColor(color='White'):
    if color == 'White':
        red.on()
        green.on()
        blue.on()
    elif color == 'Red':
        red.on()
        green.off()
        blue.off()
    elif color == 'Orange':
        green.value = 0.05
        red.value = 1.0

        blue.off()
    elif color == 'Yellow':
        green.value = 0.25
        red.value = 1.0

        blue.off()
    elif color == 'Green':
        red.off()
        green.on()
        blue.off()
    else:
        print("\nERROR: THAT IS NOT A COLOR\n")


def main():
    communityStatus, activeCases = getData()
    prevCheckTime = time.localtime(time.time())

    while True:
        displayColor(communityStatus)
        currTime = time.localtime(time.time())

        # Checks the cases every hour
        if currTime.tm_hour != prevCheckTime.tm_hour or (currTime.tm_hour == 14 and currTime.tm_min == 50):
            displayColor('White')

            communityStatus, activeCases = getData()
            prevCheckTime = currTime

        time.sleep(1)

# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO ports for the 7seg pins
# These are in order from the top segment going all the way around clockwise
# the last two segment pins are the middle segment and the dot, respectfully
segments = (11, 4, 23, 8, 7, 10, 18, 25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  220R

for s in segments:
    GPIO.setup(s, GPIO.OUT)
    GPIO.output(s, 0)

# GPIO ports for the digit 0-3 pins
digits = (22, 27, 17, 24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively

for d in digits:
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)

# Taking a segment pin to ground (0) activates that segment
digitSeg = {' ': (1,1,1,1,1,1,1,1),
           '.': (1,1,1,1,1,1,1,0),
           '0': (0,0,0,0,0,0,1,1),
           '1': (1,0,0,1,1,1,1,1),
           '2': (0,0,1,0,0,1,0,1),
           '3': (0,0,0,0,1,1,0,1),
           '4': (1,0,0,1,1,0,0,1),
           '5': (0,1,0,0,1,0,0,1),
           '6': (0,1,0,0,0,0,0,1),
           '7': (0,0,0,1,1,1,1,1),
           '8': (0,0,0,0,0,0,0,1),
           '9': (0,0,0,0,1,0,0,1)}


# try:
#     while True:
#         n = time.ctime()[11:13]+time.ctime()[14:16]
#         s = str(n).rjust(4)
#         for digit in range(4):
#             for loop in range(0,7):
#                 GPIO.output(segments[loop], num[s[digit]][loop])
#                 if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
#                     GPIO.output(25, 1)
#                 else:
#                     GPIO.output(25, 0)
#             GPIO.output(digits[digit], 0)
#             time.sleep(1)
#             GPIO.output(digits[digit], 1)
# finally:
#     GPIO.cleanup()

def displayDigit(digit):
    numP = digitSeg[digit]
    for pinLvl, seg in zip(numP, segments):
        GPIO.output(seg, pinLvl)


# Displays up to a 3-digit number
# Bringing these low will turn on the digits 0-3 (from left to right):
# [22] [27] [17] [24]
def displayNum(number):
    numDigits = len(number)
    dif = 4-numDigits
    while True:
        for i, digit in enumerate(number):
            # Turning on the right digits:
            GPIO.output(digits[i+dif], 0)
            # Displaying the digit:
            displayDigit(digit)

            time.sleep(1)
            GPIO.output(digits[i+dif], 1)

displayNum("123")


# try:
#     while True:
#         for numS, numP in num.items():
#             print(numS, numP)
#             for pinLvl, seg in zip(numP, segments):
#                 GPIO.output(seg, pinLvl)
#             time.sleep(1)
# finally:
#     GPIO.cleanup()
