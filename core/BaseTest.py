# из которого будут наследовать все тесты-это родительский
import pytest
from selenium import webdriver
import time

@pytest.fixture(scope='session')
def browser(): # отвечает за работу браузеров: открытие и закрытие
    driver = webdriver.Chrome() # запускается окно браузера
    yield driver                # ставим дальнейшее выполнение функции на паузу
    time.sleep(3)               # чтоб успеть постмотреть что происходит на странице после выполнения функции
    driver.quit()               # закрытие браузера