from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(by=By.ID, value="num1").text
    y_el = browser.find_element(by=By.ID, value="num2").text
    xy_sum = int(x_el) + int(y_el)

    select = Select(browser.find_element(by=By.TAG_NAME, value="select"))
    select.select_by_visible_text(str(xy_sum))

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    sleep(10)
    browser.quit()
