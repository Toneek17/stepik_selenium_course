from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    x = browser.find_element(by=By.ID, value="input_value").text
    y = calc(x)
    input1 = browser.find_element(by=By.ID, value="answer")
    input1.send_keys(y)
    input3 = browser.find_element(by=By.ID, value="robotCheckbox")
    input3.click()
    input4 = browser.find_element(by=By.ID, value="robotsRule")
    input4.click()

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
