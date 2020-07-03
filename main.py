from scraper import Bot

bot = Bot()
bot.requestContent()
print("Active Cases:", bot.getCases())
print("Community Status:", bot.getCommunityStatus())
