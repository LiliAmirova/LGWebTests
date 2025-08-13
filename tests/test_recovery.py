import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelper

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'email'
PASSWORD_TEXT = '1'

@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)     #открыть страницу логина
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(LOGIN_TEXT)

    for i in range(3):
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()

    RecoveryPageHelperHelper(browser)  # Проверка, что действительно перешли на нужную страницу и с нужными элементами


