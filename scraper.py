from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

LINK = "https://www.kflaph.ca/en/healthy-living/status-of-cases-in-kfla.aspx"
LINK2 = "https://app.powerbi.com/view?r=eyJrIjoiOWI2Njc5ZTctZjQ2YS00OGQ4LWEyZmEtNmU0YzBmZmM3N2YwIiwidCI6Ijk" \
        "4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9"

colorsRow = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
            "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
            "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]"

WHITE = 'rgba(255, 255, 255, 1)'    # The default background color.


class Bot:
    def __init__(self):
        op = Options()
        op.add_argument("--headless")
        op.add_argument("--disable-gpu")
        op.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=op)
        self.driver.implicitly_wait(4)

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def requestContent(self, link=LINK2):
        self.driver.get(link)

        # Switching to the right frame
        if link == LINK:
            self.driver.switch_to.frame(0)

    def getCases(self):
        print('\t', end='')
        # Getting the order of the elements:
        # I do this because the order of the elements change everyday, and so this makes it more dynamic
        elements = self.driver.find_elements_by_xpath(
            '/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/'
            'div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/'
            'visual-container-repeat/visual-container-group')

        totalCaseNumbersRow = None

        for element in elements:
            print("<", end="")
            if 'Total \nCase\nNumbers' in element.text:
                totalCaseNumbersRow = element
                break

        if totalCaseNumbersRow is None:
            print('Error, couldn\'t find Total Case Numbers row')
            return

        print("Got Total Case Numbers Row!")
        elements = totalCaseNumbersRow.find_elements_by_xpath('./transform/div/div[2]/visual-container-modern')

        numCasesResolved = 0
        numDeaths = 0
        numCasesTot = 0

        for elm in elements:
            elmText = elm.text
            # Skipping unimportant elements:
            if elmText == 'Total \nCase\nNumbers' or '# of Health Care Workers Positive' in elm.text:
                continue

            if 'Resolved' in elmText:
                numCasesResolved = int(elmText.split("\n")[0])
            elif 'Deaths' in elmText:
                numDeaths = int(elmText.split("\n")[0])
            elif 'of Cases' in elmText:
                numCasesTot = int(elmText.split("\n")[0])

        print("\tnumCasesResolved: ", numCasesResolved)
        print("\tnumDeaths: ", numDeaths)
        print("\tnumCasesTot:", numCasesTot)

        currActive = numCasesTot - numDeaths - numCasesResolved
        return currActive

    def getCommunityStatus(self):
        print('\t', end='')
        # Getting the order of the elements:
        # I do this because the order of the elements is different everyday and so this makes it more dynamic
        elements = self.driver.find_elements(By.XPATH, colorsRow + '/visual-container-modern')
        while len(elements) == 0 or len(elements[0].text) == 0:
            elements = self.driver.find_elements(By.XPATH, colorsRow + '/visual-container-modern')
            print(">", end="")
        print("Got Community Status Row!")

        for order, elm in enumerate(elements):
            if elm.text == 'Overall \nCommunity\nStatus':
                continue

            colorElm = elm.find_element(By.XPATH, ".//transform/div/div[3]/div")
            bgColor = colorElm.value_of_css_property("background-color")

            # Checking to see if that element color has been changed from its default white
            # if it has then that is the current community status
            if bgColor != WHITE:
                return colorElm.text.strip()


# print("\n", time.strftime("%d %b %H:%M:%S", time.localtime()))
# bot = Bot()
# bot.requestContent()
# communityStatus = bot.getCommunityStatus()
# activeCases = bot.getCases()
# print("Community Status:|" + communityStatus + '|')
# print("Active Cases:", activeCases)
