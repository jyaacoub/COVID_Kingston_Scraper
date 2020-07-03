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

red = PWMLED(22, frequency=100)
green = PWMLED(27, frequency=1)
blue = PWMLED(17, frequency=25)

green.value = 0.01
sleep(5)
# red.blink(n=3, background=False)
# green.blink(n=3, background=False)
# blue.blink(n=3, background=False)

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

