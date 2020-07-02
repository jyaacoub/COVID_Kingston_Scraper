import requests
from bs4 import BeautifulSoup

LINK = "https://www.kflaph.ca/en/healthy-living/status-of-cases-in-kfla.aspx"
LINK2 = "https://app.powerbi.com/view?r=eyJrIjoiNTJjYWM2NjgtNTRhZi00NDcyLTkxYzEtZDlmZTZjMDRmN2QzIiwidCI6Ijk4M2JmOTVjLTAyNDYtNDg5My05MmI4LTgwMWJkNTEwYjRmYSJ9"

# Xpath for the active covid cases number
# "/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-group[1]/transform/div/div[2]/visual-container-modern[1]/transform/div/div[3]/div/visual-modern/div/svg/g[1]/text/tspan"

def main():
    response = requests.get(LINK2)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

main()
