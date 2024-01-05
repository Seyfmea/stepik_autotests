from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), ("100")))
book = browser.find_element(By.ID, "book")
book.click()


x = int(browser.find_element(By.ID, 'input_value').text)
answer = log(abs(12 * sin(x)))

input_field = browser.find_element(By.ID, 'answer')
input_field.send_keys(answer)

submit = browser.find_element(By.ID, 'solve')
submit.click()

time.sleep(5)
