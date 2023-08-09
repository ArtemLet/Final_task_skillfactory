# Иоговый проект по курсу тестировщик-автоматизатор QAP Skillfactory. Тестирование формы авторизации сервиса "Ростелеком".

Обьект тестирования: [https://b2c.passport.rt.ru](https://b2c.passport.rt.ru)  
Требования: [Требования для тестирования](https://docs.google.com/document/d/12yoTwHSTXxIUQQCH32OvlSd3QYUt_aQk/edit)  

Файлы
-----
[chromedriver-win64/chromedriver.exe](chromedriver-win64/chromedriver.exe) Веб-драйвер браузера Google Chrome  
[tests/conftest.py](tests/conftest.py) Фикстуры для выполнения тестов  
[tests/test_auth.py](tests/test_auth.py) Содержит тесты веб-интерфейса  
[settings.py](settings.py) Настройка переменных окружения  
[requirements.txt](requirements.txt) Необходимые библиотеки для работы тестов. Установка: pip3 install -r requirements  
[pages/base_page.py](pages/base_page.py) Класс базовой страницы, с базовыми функциями  
[pages/auth_page.py](pages/auth_page.py) Класс страницы авторизации, содержит необходимые локаторы и функции  
[pages/user_page.py](pages/user_page.py) Класс страницы профиля пользователя, содержит необходимые локаторы и функции  
[pages/registration_page.py](pages/registration_page.py) Класс страницы регистрации, содержит необходимые локаторы и функции  
[chromedriver-win64/chromedriver.exe](chromedriver-win64/chromedriver.exe) Веб-драйвер браузера Google Chrome  

Запуск тестов
-------------
1) Установить все необходимые библиотеки: pip3 install -r requirements
2) Загрузить [Selenium WebDriver](https://chromedriver.chromium.org/downloads) (выбрать версию совместимую с вашим браузером)
3) Запуск тестов: python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/test_auth.py
