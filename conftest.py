import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": "en"})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()


    yield browser
    print("\nquit browser..")
    browser.quit()