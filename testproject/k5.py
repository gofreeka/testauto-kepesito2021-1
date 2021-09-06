from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
time.sleep(2)

play_bt = driver.find_element_by_id('spin')
init_bt = driver.find_element_by_id('init')

# * Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz


def test_tc01():
    pass

# * Bingo számok ellenőzrzése:
#     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott
#     számok közül kerültek-e ki


def test_tc02():
    play_bt.click()


# * Új játékot tudunk indítani
#     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     * új bingo szelvényt kapunk más számokkal.

def test_tc03():
    init_bt.click()


test_tc01()
test_tc02()
test_tc03()

# driver.close()
