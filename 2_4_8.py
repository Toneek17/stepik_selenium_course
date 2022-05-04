from time import sleep
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5) неявное ожидание
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(by=By.ID, value="book").click()

    x_el = int(browser.find_element(by=By.ID, value="input_value").text)
    x = calc(x_el)
    browser.find_element(by=By.ID, value="answer").send_keys(x)
    browser.find_element(by=By.ID, value="solve").click()

finally:
    sleep(10)
    browser.quit()
