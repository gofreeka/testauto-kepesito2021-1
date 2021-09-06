from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
time.sleep(2)

# ## 1 Feladat: Pitagorasz-tétel
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Pitagorasz-tétel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#

# Elements
input_a = driver.find_element_by_id('a')
input_b = driver.find_element_by_id('b')
result_c = driver.find_element_by_id('result')
results = driver.find_element_by_id('results')
bt_submit = driver.find_element_by_id('submit')


# Test data
test_data_tc01 = ['', '', '']
test_data_tc02 = ['2', '3', '10']
test_data_tc03 = ['', '', 'NaN']

# input elemek kiuritese


def clear_inputs():
    input_a.clear()
    input_b.clear()

# * Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik>


def test_tc01():
    input_a.send_keys(test_data_tc01[0])
    input_b.send_keys(test_data_tc01[1])
    # bt_submit.click()

    assert not results.is_displayed()

# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10


def test_tc02():
    clear_inputs()
    input_a.send_keys(test_data_tc02[0])
    input_b.send_keys(test_data_tc02[1])
    bt_submit.click()

    assert result_c.text == test_data_tc02[2]


# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN


def test_tc03():
    clear_inputs()
    input_a.send_keys(test_data_tc03[0])
    input_b.send_keys(test_data_tc03[1])
    bt_submit.click()

    assert result_c.text == test_data_tc03[2]


test_tc01()
test_tc02()
test_tc03()
