from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
time.sleep(2)

# ## 2 Feladat: Színes reakció

# Elements
bt_start = driver.find_element_by_id('start')
bt_stop = driver.find_element_by_id('stop')
random_color_name = driver.find_element_by_id('randomColorName')
random_color_background = driver.find_element_by_id('randomColor')
test_color_background = driver.find_element_by_id('testColor')
test_color_name = driver.find_element_by_id('testColorName')
result = driver.find_element_by_id('result')

# Test data
test_data_tc01 = ['']
test_data_tc03 = ['Incorrect!', 'Correct!']


# * Helyesen jelenik meg az applikáció betöltéskor:
#   * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#     <szín neve> [     ] == [     ]


def test_tc01():
    assert random_color_name.text != test_data_tc01[0]


# * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.


def test_tc02():
    bt_start.click()
    time.sleep(2)
    assert test_color_name.text != ''
    bt_stop.click()


# * Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.


def test_tc03():
    bt_start.click()
    time.sleep(2)
    if result.text == test_data_tc03[0]:
        print(result.text)
    else:
        bt_stop.click()
        print(result.text)


# test_tc01()
# test_tc02()
# test_tc03()

# driver.close()
