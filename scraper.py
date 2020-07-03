from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options

LINK = "https://www.kflaph.ca/en/healthy-living/status-of-cases-in-kfla.aspx"
LINK2 = "https://app.powerbi.com/view?r=eyJrIjoiNTJjYWM2NjgtNTRhZi00NDcyLTkxYzEtZDlmZTZjMDRmN2QzIiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9"


class Bot:
    def __init__(self):
        op = Options()
        # op.add_argument("--headless")
        op.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=op)
        self.driver.implicitly_wait(4)

    def requestContent(self, link):
        self.driver.get(link)

    def getCases(self):
        pass

    def getColor(self):
        pass

bot = Bot()
bot.requestContent(LINK)
print(bot.driver.find_element(By.XPATH, "/html/body"))

