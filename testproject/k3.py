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

# Elements
title_input = driver.find_element_by_id('title')
error_msg = driver.find_element_by_xpath('/html/body/form/span')
no_error = driver.find_element_by_xpath("//form/span[@class='error']")


# Test data
test_data_01 = ['abcd1234', '']
test_data_02 = ['teszt233@', 'Only a-z and 0-9 characters allewed']
test_data_03 = ['abcd', 'Title should be at least 8 characters; you entered 4.']

# Title mezo kiuritese


def input_clear():
    title_input.clear()


# * Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet


def test_tc01():
    title_input.send_keys(test_data_01[0])
    print(no_error.text)

# * Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allewed.


def test_tc02():
    input_clear()
    title_input.send_keys(test_data_02[0])
    assert error_msg.text == test_data_02[1]


# * Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.


def test_tc03():
    input_clear()
    title_input.send_keys(test_data_03[0])
    assert error_msg.text == test_data_03[1]


test_tc01()
test_tc02()
test_tc03()

# driver.close()
