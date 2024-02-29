from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

browser.get(link)

journey_button = browser.find_element(By.CLASS_NAME, 'btn')
journey_button.click()

confirm = browser.switch_to.alert
confirm.accept()
x = int(browser.find_element(By.ID, 'input_value').text)

answer = log(abs(12 * sin(x)))

input_field = browser.find_element(By.CLASS_NAME, 'form-control')
input_field.send_keys(answer)

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()

time.sleep(5)