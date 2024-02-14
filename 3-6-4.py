from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'https://stepik.org/lesson/236895/step/1'
browser.get(link)
browser.implicitly_wait(5)

def test_login_stepik():

    login_button = browser.find_element(By.ID, "ember35")
    login_button.click()

    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys("")

    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys("")

    submit_btn = browser.find_element(By.CLASS_NAME, "button_with-loader")
    submit_btn.click()

    popup = browser.find_element(By.CLASS_NAME, "light-tabs")
    WebDriverWait(browser, 3).until(EC.invisibility_of_element(popup))

    time.sleep(3)