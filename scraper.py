from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

LINK = "https://www.kflaph.ca/en/healthy-living/status-of-cases-in-kfla.aspx"
LINK2 = "https://app.powerbi.com/view?r=eyJrIjoiNTJjYWM2NjgtNTRhZi00NDcyLTkxYzEtZDlmZTZjMDRmN2QzIiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9"


casesRow = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
             "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
             "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[8]/transform/div/div[2]"

casesXPATH = casesRow + "/visual-container-modern[{case}]"

colorsRow = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
            "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
            "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]"


colorsXPATH = colorsRow + "/visual-container-modern[{color}]/transform/div/div[3]/div"

WHITE = 'rgba(255, 255, 255, 1)'    # The background color for white


class Bot:
    def __init__(self):
        op = Options()
        op.add_argument("--headless")
        op.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=op)
        self.driver.implicitly_wait(4)

    def refreshPage(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def requestContent(self, link=LINK2):
        self.driver.get(link)

    def getCases(self):
        print('\t', end='')
        # Getting the order of the elements:
        # I do this because the order of the elements change everyday, and so this makes it more dynamic
        elements = self.driver.find_elements(By.XPATH, casesRow + '/visual-container-modern')
        while elements[0].text == '':
            elements = self.driver.find_elements(By.XPATH, casesRow + '/visual-container-modern')
            print("<", end="")
        print("Got Total Case Numbers Row!")

        numCasesResolved = ''
        numDeaths = ''
        numCasesTot = ''

        for order, elm in enumerate(elements):
            elmText = elm.text
            # Skipping unimportant elements:
            if elmText == 'Total \nCase\nNumbers' or '# of Health Care Workers Positive' in elm.text:
                continue

            if 'Resolved' in elmText:
                numCasesResolved = int(elmText.split("\n")[0])
            elif 'Deaths' in elmText:
                numDeaths = int(elmText.split("\n")[0])
            else:
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
        while elements[0].text == '':
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
