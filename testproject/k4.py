from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)
time.sleep(2)


# * Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~


def test_tc01():
    pass


# * Megjelenik egy érvényes művelet:
#     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * `op` mező vagy + vagy - karaktert tartlamaz
#     * `num` mező egy egész számot tartalamaz

def test_tc02():
    pass


# * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#     * A `num` mezőben megjelenő mennyiségű karaktert
#     * az `result` mező helyes karaktert fog mutatni

def test_tc03():
    pass

