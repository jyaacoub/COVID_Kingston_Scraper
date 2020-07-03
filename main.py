from scraper import Bot

# bot = Bot()
# bot.requestContent()
# print("Active Cases:", bot.getCases())
# print("Community Status:", bot.getCommunityStatus())
from gpiozero import LED, PWMLED
from time import sleep

# red = LED(22)
# green = LED(27)
# blue = LED(17)
PWMLED(17, frequency=100)
sleep(3)
PWMLED(17, frequency=50)
sleep(3)
PWMLED(17, frequency=25)
sleep(3)
PWMLED(17, frequency=10)
sleep(3)
PWMLED(17, frequency=1)


# Sub in 2 for Red, 3-Orange, 4-Yellow, and 5-Green
# while True:
#     # Red
#     red.on()
#     sleep(1)
#
#     # Orange
#     # TODO: Figure out how to display orange with rgb led.
#
#
#     # Yellow
#     green.on()
#     sleep(1)
#
#     # Green
#     red.off()
#     sleep(1)
#
#     green.off()

