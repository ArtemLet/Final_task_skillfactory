from settings import valid_email, valid_password, valid_phone, valid_login, valid_account

"""Открытие формы авторизации"""


def test_auth_page_opening(browser, auth_page):
    auth_page.go_to_site()
    page_name = auth_page.get_auth_page_name()
    assert page_name == "Авторизация"


"""RT-001 Форма авторизации разделена на две секции"""


def test_auth_page_separation(browser, auth_page):
    auth_page.go_to_site()
    left_section = auth_page.get_auth_page_left_section()
    right_section = auth_page.get_auth_page_right_section()
    assert left_section and right_section


"""RT-002 Левая часть формы авторизации содержит логотип, заголовок: "Личный кабинет" и вспомогательную информацию"""


def test_auth_left_section_elems(browser, auth_page):
    auth_page.go_to_site()
    elems = auth_page.get_auth_page_left_section_elems()
    assert "Личный кабинет" in elems and elems


"""RT-003 Правая секция формы авторизации содержит типы аутентификации: Телефон, Почта, Логин, Лицевой счёт"""


def test_auth_page_left_section_auth_types(browser, auth_page):
    auth_page.go_to_site()
    tabs = auth_page.get_auth_tabs_names()
    assert "Телефон" and "Почта" and "Логин" and "Лицевой счёт" in tabs


"""RT-004 Наличие полей ввода логина и пароля"""


def test_auth_fields(browser, auth_page):
    auth_page.go_to_site()
    login = auth_page.get_auth_login_field()
    password = auth_page.get_auth_pass_field()
    assert login and password


"""RT-005 По умолчанию открывается авторизация по номеру мобильного телефона"""


def test_auth_fields_names(browser, auth_page):
    auth_page.go_to_site()
    login = auth_page.get_auth_login_field_name()
    assert "Мобильный телефон" in login


"""RT-006 Открытие вкладки авторизации Почта"""


def test_auth_email_open(browser, auth_page):
    auth_page.go_to_site()
    auth_page.open_auth_email()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Электронная почта" in login_field_name


"""RT-007 Открытие вкладки авторизации Логин"""


def test_auth_login_open(browser, auth_page):
    auth_page.go_to_site()
    auth_page.open_auth_login()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Логин" in login_field_name


"""RT-008 Открытие вкладки авторизации Лицевой счёт"""


def test_auth_account_open(browser, auth_page):
    auth_page.go_to_site()
    auth_page.open_auth_account()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Лицевой счёт" in login_field_name


"""RT-009 Автоматическая смена вкладки авторизации на Мобильный телефон при вводе номера телефона"""


def test_auth_auto_switch_tab_phone(browser, auth_page):
    auth_page.go_to_site()
    auth_page.open_auth_email()
    auth_page.get_auth_login_field().send_keys("+79991112222")
    auth_page.get_auth_pass_field().click()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Мобильный телефон" in login_field_name


"""RT-010 Автоматическая смена вкладки авторизации на Почта при вводе электронной почты"""


def test_auth_auto_switch_tab_email(browser, auth_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys("test@mail.ru")
    auth_page.get_auth_pass_field().click()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Электронная почта" in login_field_name


"""RT-011 Автоматическая смена вкладки авторизации на Логин при вводе логина"""


def test_auth_auto_switch_tab_login(browser, auth_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys("test_user")
    auth_page.get_auth_pass_field().click()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Логин" in login_field_name


"""RT-012 Автоматическая смена вкладки авторизации на Лицевой счёт при вводе номера лицевого счета"""


def test_auth_auto_switch_tab_account(browser, auth_page):
    auth_page.go_to_site()
    auth_page.open_auth_email()
    auth_page.get_auth_login_field().send_keys("012345678910")
    auth_page.get_auth_pass_field().click()
    login_field_name = auth_page.get_auth_login_field_name()
    assert "Лицевой счёт" in login_field_name


"""RT-013 Авторизация клиента по номеру телефона с валидными данными"""


def test_auth_phone_with_valid_data(browser, auth_page, user_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys(valid_phone)
    auth_page.get_auth_pass_field().send_keys(valid_password)
    auth_page.click_auth_btn()
    assert user_page.get_user_page_logout_btn()


"""RT-014 Авторизация клиента по адресу электронной почты с валидными данными"""


def test_auth_email_with_valid_data(browser, auth_page, user_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys(valid_email)
    auth_page.get_auth_pass_field().send_keys(valid_password)
    auth_page.click_auth_btn()
    assert user_page.get_user_page_logout_btn()


"""RT-015 Авторизация клиента по Логину с валидными данными"""


def test_auth_login_with_valid_data(browser, auth_page, user_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys(valid_login)
    auth_page.get_auth_pass_field().send_keys(valid_password)
    auth_page.click_auth_btn()
    assert user_page.get_user_page_logout_btn()


"""RT-016 Авторизация клиента по номеру лицевого счета с валидными данными"""


def test_auth_account_with_valid_data(browser, auth_page, user_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys(valid_account)
    auth_page.get_auth_pass_field().send_keys(valid_password)
    auth_page.click_auth_btn()
    assert user_page.get_user_page_logout_btn()


"""RT-017 При нажатии на ссылку "Зарегистрироваться" осуществляется переход на страницу регистрации"""


def test_auth_reg_btn(browser, auth_page, reg_page):
    auth_page.go_to_site()
    auth_page.click_reg_link()
    assert "Регистрация" in reg_page.get_reg_page_header()


"""RT-018 При нажатии на кнопку "Выйти" в профиле пользователя, осуществляется выход из профиля и
 переход на страницу авторизации"""


def test_user_page_logout_btn(browser, auth_page, user_page):
    auth_page.go_to_site()
    auth_page.get_auth_login_field().send_keys(valid_email)
    auth_page.get_auth_pass_field().send_keys(valid_password)
    auth_page.click_auth_btn()
    user_page.get_user_page_logout_btn().click()
    assert "Авторизация" in auth_page.get_auth_page_name()


def test_auth_with_vk_id(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_vk_btn()
    assert auth_page.get_link().hostname == 'id.vk.com'


def test_auth_with_ok(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_ok_btn()
    assert auth_page.get_link().hostname == 'connect.ok.ru'


def test_auth_with_mail(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_mail_btn()
    assert auth_page.get_link().hostname == 'connect.mail.ru'


def test_auth_with_ya_id(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_ya_btn()
    assert auth_page.get_link().hostname == 'passport.yandex.ru'
