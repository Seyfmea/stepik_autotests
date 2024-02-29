from selenium.webdriver.common.by import By
from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

browser.get(link)

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

time.sleep(2)

x = int(browser.find_element(By.ID, 'input_value').text)

answer = log(abs(12 * sin(x)))

input_field = browser.find_element(By.ID, 'answer')
input_field.send_keys(answer)

submit = browser.find_element(By.CLASS_NAME, 'btn')
submit.click()

time.sleep(5)
