from selenium.webdriver.common.by import By

from pages.base_page import BasePage

"""Класс страницы профиля пользователя"""


class UserPage(BasePage):
    """Локаторы"""
    LOCATOR_USER_PAGE_LOGOUT = (By.ID, 'logout-btn')

    """Получение кнопки выхода из профиля"""

    def get_user_page_logout_btn(self):
        return self.find_element(self.LOCATOR_USER_PAGE_LOGOUT)
