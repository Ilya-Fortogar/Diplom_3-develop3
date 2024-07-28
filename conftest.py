import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        driver = webdriver.Chrome()
    elif 'firefox' in request.param:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
