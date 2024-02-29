from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def summ(num1, num2):
    return str(int(num1) + int(num2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    select = Select(browser.find_element(By.ID, "dropdown"))
    summa = summ(num1, num2)
    select.select_by_value(summa)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()
