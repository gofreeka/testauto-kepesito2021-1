from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
time.sleep(2)


# * Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet


def test_tc01():
    pass

# * Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allewed.


def test_tc02():
    pass


# * Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.


def test_tc03():
    pass

