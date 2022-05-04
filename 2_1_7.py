from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(1)

    x_el = browser.find_element(by=By.ID, value="treasure")
    x = x_el.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(by=By.ID, value="answer")
    input1.send_keys(y)
    input3 = browser.find_element(by=By.ID, value="robotCheckbox")
    input3.click()
    input4 = browser.find_element(by=By.ID, value="robotsRule")
    input4.click()

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    sleep(1)

finally:
    sleep(5)
    browser.quit()
