from selenium.webdriver.common.by import By

from pages.base_page import BasePage

"""Класс страница авторизации"""


class AuthPage(BasePage):
    """Локаторы"""
    LOCATOR_AUTH_PAGE_NAME = (By.CLASS_NAME, "card-container__title")
    LOCATOR_AUTH_TABS = (By.CLASS_NAME, 'rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')
    LOCATOR_AUTH_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_AUTH_EMAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOCATOR_AUTH_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_ACCOUNT_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_AUTH_LEFT_SECTION_LOGO = (By.CLASS_NAME, 'what-is-container__logo-container')
    LOCATOR_AUTH_LEFT_SECTION_NAME = (By.CLASS_NAME, 'what-is__title')
    LOCATOR_AUTH_LEFT_SECTION_ADDITIONAL_INFO = (By.CLASS_NAME, 'what-is__desc')
    LOCATOR_AUTH_LOGIN_FIELD_NAME = (By.CLASS_NAME, 'rt-input.rt-input--rounded.rt-input--orange')
    LOCATOR_AUTH_PASS_FIELD_NAME = (By.CLASS_NAME, 'rt-input.rt-input--rounded.rt-input--orange.rt-input--actions')
    LOCATOR_AUTH_PASS = (By.ID, 'password')
    LOCATOR_AUTH_USERNAME = (By.ID, 'username')
    LOCATOR_AUTH_BTN = (By.ID, 'kc-login')
    LOCATOR_AUTH_LEFT_SECTION = (By.ID, 'page-left')
    LOCATOR_AUTH_RIGHT_SECTION = (By.ID, 'page-right')
    LOCATOR_AUTH_PAGE_REGISTRATION_LINK = (By.ID, 'kc-register')
    LOCATOR_AUTH_PAGE_VK = (By.ID, 'oidc_vk')
    LOCATOR_AUTH_PAGE_OK = (By.ID, 'oidc_ok')
    LOCATOR_AUTH_PAGE_MAIL = (By.ID, 'oidc_mail')
    LOCATOR_AUTH_PAGE_YA = (By.ID, 'oidc_ya')
    LOCATOR_YA_ID_PAGE = (By.ID, 'passp-field-phone')

    """Получение имени страницы авторизации"""

    def get_auth_page_name(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_NAME).text

    """Получение текста левой секции"""

    def get_auth_left_section_name(self):
        return self.find_element(self.LOCATOR_AUTH_LEFT_SECTION_NAME).text

    """Получение названий переключателей типа аутентификации"""

    def get_auth_tabs_names(self):
        return self.find_element(self.LOCATOR_AUTH_TABS).text

    """Получение левой части страницы авторизации"""

    def get_auth_page_left_section(self):
        return self.find_element(self.LOCATOR_AUTH_LEFT_SECTION)

    """Получение правой части страницы авторизации"""

    def get_auth_page_right_section(self):
        return self.find_element(self.LOCATOR_AUTH_RIGHT_SECTION)

    """Получение поля ввода логина"""

    def get_auth_login_field(self):
        return self.find_element(self.LOCATOR_AUTH_USERNAME)

    """Получение поля ввода пароля"""

    def get_auth_pass_field(self):
        return self.find_element(self.LOCATOR_AUTH_PASS)

    """Получение названия поля ввода логина"""

    def get_auth_login_field_name(self):
        return self.find_element(self.LOCATOR_AUTH_LOGIN_FIELD_NAME).text

    """Получение названия поля ввода пароля"""

    def get_auth_pass_field_name(self):
        return self.find_element(self.LOCATOR_AUTH_PASS_FIELD_NAME).text

    """Получение логотипа, названия и поля дополнительной информацией в левой секции"""

    def get_auth_page_left_section_elems(self):
        logo = self.find_element(self.LOCATOR_AUTH_LEFT_SECTION_LOGO)
        name = self.find_element(self.LOCATOR_AUTH_LEFT_SECTION_NAME).text
        additional_info = self.find_element(self.LOCATOR_AUTH_LEFT_SECTION_ADDITIONAL_INFO)
        return logo, name, additional_info

    """Открытие вкладки авторизации Почта"""

    def open_auth_email(self):
        return self.find_element(self.LOCATOR_AUTH_EMAIL_TAB).click()

    """Открытие вкладки авторизации Логин"""

    def open_auth_login(self):
        return self.find_element(self.LOCATOR_AUTH_LOGIN_TAB).click()

    """Открытие вкладки авторизации Лицевой счёт"""

    def open_auth_account(self):
        return self.find_element(self.LOCATOR_AUTH_ACCOUNT_TAB).click()

    """Нажатие кнопки Войти"""

    def click_auth_btn(self):
        return self.find_element(self.LOCATOR_AUTH_BTN).click()

    """Нажатие ссылки Зарегистрироваться"""

    def click_reg_link(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_REGISTRATION_LINK).click()

    """Нажатие кнопки VK"""

    def click_vk_btn(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_VK).click()

    """Нажатие кнопки Одноклассники"""

    def click_ok_btn(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_OK).click()

    """Нажатие кнопки Mail.ru"""

    def click_mail_btn(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_MAIL).click()

    """Нажатие кнопки Yandex"""

    def click_ya_btn(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_YA).click()
