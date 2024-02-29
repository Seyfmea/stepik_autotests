import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#browser = webdriver.Chrome()
answer = math.log(int(time.time()))


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_parametrization(driver, link):
    driver.implicitly_wait(10)

    wait = WebDriverWait(driver, 15)
    url = f'{link}'
    driver.get(url)

    login_button = driver.find_element(By.ID, "ember35")
    login_button.click()

    email_field = driver.find_element(By.ID, "id_login_email")
    email_field.send_keys("")

    password_field = driver.find_element(By.ID, "id_login_password")
    password_field.send_keys("")

    submit_btn = driver.find_element(By.CLASS_NAME, "button_with-loader")
    submit_btn.click()
    #time.sleep(4)

    #textarea = driver.find_element(By.CLASS_NAME, 'textarea')
    textarea = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'textarea')))
    textarea.send_keys(answer)
    #time.sleep(2)

    submit_rslt = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'submit-submission')))
    submit_rslt.click()

    #hint = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'lesson-hint'), 'Correct!'))
    #hint = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'lesson-hint')))
    hint = driver.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert hint == 'Correct!'
    #time.sleep(500)
