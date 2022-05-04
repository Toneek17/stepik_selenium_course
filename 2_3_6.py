from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()
    window2 = browser.window_handles[1]
    window1 = browser.window_handles[0]
    browser.switch_to.window(window2)
    x_el = int(browser.find_element(by=By.ID, value="input_value").text)
    x = calc(x_el)
    browser.find_element(by=By.ID, value="answer").send_keys(str(x))
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()

finally:
    sleep(10)
    browser.quit()
