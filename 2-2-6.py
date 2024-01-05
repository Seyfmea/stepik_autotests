from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log
import time

def formula(x):
    answer = log(abs(12 * sin(x)))
    return answer

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(formula(x))
    browser.execute_script('window.scrollTo(0,250)')

    checkbox = browser.find_element(By. CSS_SELECTOR, '.form-check-custom .form-check-label')
    checkbox.click()

    radiobutton = browser.find_element(By. ID, 'robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()



finally:
    time.sleep(7)
    browser.quit()