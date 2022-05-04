from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(by=By.NAME, value="firstname").send_keys("Ivan")
    browser.find_element(by=By.NAME, value="lastname").send_keys("Petrov")
    browser.find_element(by=By.NAME, value="email").send_keys("ipetrov@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element(by=By.NAME, value="file").send_keys(file_path)
    browser.find_element(by=By.CSS_SELECTOR, value="button.btn").click()

finally:
    sleep(10)
    browser.quit()
