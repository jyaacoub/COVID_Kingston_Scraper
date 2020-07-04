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
colorsRow = "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/" \
            "exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/" \
            "div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]"

colorsXPATH = colorsRow + "/visual-container-modern[{color}]/transform/div/div[3]/div"


WHITE = 'rgba(255, 255, 255, 1)'    # The background color for white

# "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]/visual-container-modern[4]/transform/div/div[3]/div/visual-modern/div"
# "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]/visual-container-modern[2]/transform/div/div[3]/div/visual-modern/div"
# "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]/visual-container-modern[3]/transform/div/div[3]/div/visual-modern/div"
# "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[3]/transform/div/div[2]/visual-container-modern[5]/transform/div/div[3]/div"
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
        # getting the order of the elements:
        elements = self.driver.find_elements(By.XPATH, colorsRow+'/visual-container-modern')
        while elements[0].text == '':
            elements = self.driver.find_elements(By.XPATH, colorsRow+'/visual-container-modern')

        for elm in elements:
            print(elm.text, "\n________")

        for order, elm in enumerate(elements):
            print(order, elm.text)
            if elm.text == 'Overall \nCommunity\nStatus':
                continue
            colorElm = elm.find_element(By.XPATH, ".//transform/div/div[3]/div")
            print(colorElm.text, end=" | ")

            bgcolor = colorElm.value_of_css_property("background-color")
            print(bgcolor, "\n______________")
            # Checking to see if that element color has been changed from its default white
            # if it has then that is the current community status
            if bgcolor != WHITE:
                return colorElm.text


bot = Bot()
bot.requestContent()
print("community staus: ", bot.getCommunityStatus())
