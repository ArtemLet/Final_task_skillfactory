import pytest
from pages.auth_page import AuthPage
from pages.registration_page import RegPage
from pages.user_page import UserPage
from selenium import webdriver

"""Инициализация браузера и открытие страницы авторизации"""


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


"""Создание экземпляра класса AuthPage"""


@pytest.fixture(scope="session")
def auth_page(browser):
    auth_page = AuthPage(browser)
    return auth_page


"""Создание экземпляра класса UserPage"""


@pytest.fixture(scope="session")
def user_page(browser):
    user_page = UserPage(browser)
    return user_page


"""Создание экземпляра класса RegPage"""


@pytest.fixture(scope="session")
def reg_page(browser):
    reg_page = RegPage(browser)
    return reg_page
