from selenium.webdriver.common.by import By

from pages.base_page import BasePage

"""Класс страницы регистрации"""


class RegPage(BasePage):
    """Локаторы"""
    LOCATOR_REG_PAGE_HEADER = (By.CLASS_NAME, 'card-container__title')

    """Получение имени заголовка страницы регистрации"""

    def get_reg_page_header(self):
        return self.find_element(self.LOCATOR_REG_PAGE_HEADER).text
