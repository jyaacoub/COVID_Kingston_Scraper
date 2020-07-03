from scraper import Bot

# bot = Bot()
# bot.requestContent()
# print("Active Cases:", bot.getCases())
# print("Community Status:", bot.getCommunityStatus())
from gpiozero import LED
from time import sleep

red = LED(22)
green = LED(27)
blue = LED(17)

while True:
    red.on()
    sleep(1)
    green.on()
    sleep(1)
    blue.on()
    sleep(1)

    red.off()
    sleep(1)
    green.off()
    sleep(1)
    blue.off()
    sleep(1)