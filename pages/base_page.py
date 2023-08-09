from urllib.parse import urlparse

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import URL

"""Класс базовой страницы"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL or 'https://b2c.passport.rt.ru'

    """Переход на сайт"""

    def go_to_site(self):
        return self.driver.get(self.base_url)

    """Находит элемент по указанному локатору"""

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Not found {locator}")

    """Находит элементы по указанному локатору"""

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Not found {locator}")

    """Получение текущего URL"""

    def get_link(self):
        url = urlparse(self.driver.current_url)
        return url
