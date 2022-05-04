from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    m = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(by=By.PARTIAL_LINK_TEXT, value=m)
    link.click()

    input1 = browser.find_element(by=By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by=By.CLASS_NAME, value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by=By.ID, value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
