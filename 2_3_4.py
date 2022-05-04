from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()
    browser.switch_to.alert.accept()
    x_el = int(browser.find_element(by=By.ID, value="input_value").text)
    x = calc(x_el)
    browser.find_element(by=By.ID, value="answer").send_keys(str(x))
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()

finally:
    sleep(10)
    browser.quit()
