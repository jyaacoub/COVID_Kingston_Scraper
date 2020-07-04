from scraper import Bot

# bot = Bot()
# bot.requestContent()
# print("Active Cases:", bot.getCases())
# print("Community Status:", bot.getCommunityStatus())
from gpiozero import LED, PWMLED
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



# red = LED(22)
# green = LED(27)
# blue = LED(17)


# Sub in 2 for Red, 3-Orange, 4-Yellow, and 5-Green
while True:
    # # Red
    displayColor('r')
    sleep(1)

    # Orange
    displayColor('o')
    sleep(1)

    # Yellow
    displayColor('y')
    sleep(1)

    # # Green
    displayColor('g')
    sleep(1)

