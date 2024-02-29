from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div > h1")
    ALERT_PRODUCT_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.XPATH , '//*[@id="messages"]/div[1]/div')
