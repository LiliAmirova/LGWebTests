# из которого будут наследовать все тесты-это родительский
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser(): # отвечает за работу браузеров: открытие и закрытие
    driver = webdriver.Chrome() # запускается окно браузера
    yield driver                # ставим дальнейшее выполнение функции на паузу
    driver.quit()               # закрытие браузера

