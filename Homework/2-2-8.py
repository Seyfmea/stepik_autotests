from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/file_input.html'

browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
first_name.send_keys('123')

last_name = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
last_name.send_keys('123')

email = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
email.send_keys("123@gmail.com")

choose_file = browser.find_element(By.ID, 'file')
choose_file.send_keys(file_path)

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()

time.sleep(7)