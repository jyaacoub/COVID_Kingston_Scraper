from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

LINK = "https://www.kflaph.ca/en/healthy-living/status-of-cases-in-kfla.aspx"
LINK2 = "https://app.powerbi.com/view?r=eyJrIjoiNTJjYWM2NjgtNTRhZi00NDcyLTkxYzEtZDlmZTZjMDRmN2QzIiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9"

# Sub in 2 for the number of cases resolved or 5 for the number of cases total.
casesXPATH = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
             "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
             "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[8]/transform/div/div[2]/" \
             "visual-container-modern[{case}]"

# Sub in 2 for Red, 3-Orange, 4-Yellow, and 5-Green
colorsXPATH = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
              "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
              "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]/" \
              "visual-container-modern[{color}]/transform/div/div[3]/div"

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

    def shutdownBot(self):
        self.driver.quit()

    def requestContent(self, link=LINK2):
        self.driver.get(link)

    def getCases(self):
        numCasesLine = ''
        numCasesResolvedLine = ''

        # Polls the site until I get the data needed
        while numCasesLine == '':
            try:
                numCasesLine = self.driver.find_element(By.XPATH, casesXPATH.format(case=4)).text
            except:
                numCasesLine = self.driver.find_element(By.XPATH, casesXPATH.format(case=5)).text

        while numCasesResolvedLine == '':
            try:
                numCasesResolvedLine = self.driver.find_element(By.XPATH, casesXPATH.format(case=3)).text
            except:
                numCasesResolvedLine = self.driver.find_element(By.XPATH, casesXPATH.format(case=2)).text

        numCases = int(numCasesLine.split("\n")[0])
        numCasesResolved = int(numCasesResolvedLine.split("\n")[0])
        currActive = numCases - numCasesResolved

        return currActive

    def getCommunityStatus(self):
        red = self.driver.find_element(By.XPATH, colorsXPATH.format(color=2))

        # while loop ensures that the page has properly loaded before getting data.
        while red.text == '':
            red = self.driver.find_element(By.XPATH, colorsXPATH.format(color=2))
        red = red.value_of_css_property("background-color")
        # Checking to see if that element color has been changed from its default white
        # if it has then that is the current community status
        if red != WHITE:
            return "red"

        orange = self.driver.find_element(By.XPATH, colorsXPATH.format(color=3))

        # while loop ensures that the page has properly loaded before getting data.
        while orange.text == '':
            orange = self.driver.find_element(By.XPATH, colorsXPATH.format(color=3))
        orange = orange.value_of_css_property("background-color")
        if orange != WHITE:
            return "orange"

        yellow = self.driver.find_element(By.XPATH, colorsXPATH.format(color=4))

        # while loop ensures that the page has properly loaded before getting data.
        while yellow.text == '':
            yellow = self.driver.find_element(By.XPATH, colorsXPATH.format(color=4))
        yellow = yellow.value_of_css_property("background-color")

        if yellow != WHITE:
            return "yellow"

        green = self.driver.find_element(By.XPATH, colorsXPATH.format(color=5))

        # while loop ensures that the page has properly loaded before getting data.
        while green.text == '':
            green = self.driver.find_element(By.XPATH, colorsXPATH.format(color=5))
        green = green.value_of_css_property("background-color")
        if green != WHITE:
            return 'green'


# git p
