from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = int(browser.find_element(by=By.ID, value="input_value").text)
    x = calc(x_el)
    browser.find_element(by=By.ID, value="answer").send_keys(x)
    browser.find_element(by=By.ID, value="robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(by=By.ID, value="robotsRule").click()
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()

finally:
    sleep(10)
    browser.quit()
