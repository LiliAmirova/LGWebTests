from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random
import string

class LoginPageLocators:
    ENTRANCE_PANEL = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE_PANEL = (By.XPATH, '//*[@data-l="t,qr_tab"]')

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')

    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')

    QA_GET = (By.XPATH, '//*[@data-l="t,get_qr"]')

    # Какой из вариантов  ниже лучше использовать ?
    NE_POLUCHAYETSYA_VOYTI_1 = (By.XPATH, '//*[@class="lp"]')
    NE_POLUCHAYETSYA_VOYTI_2 = (By.XPATH, '//div[@class="recovery-link"]/a[@data-l="t,register"]')

    # Какой из вариантов  ниже лучше использовать ?
    REGISTRATION_BUTTON_1 = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]' )
    REGISTRATION_BUTTON_2 = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')

    VK_ENTRANCE = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_ENTRANCE = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_ENTRANCE = (By.XPATH, '//*[@data-l="t,yandex"]')

    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self): # функция, которая проверяет страницу на наличие и видимость элементов по локаторам, которые отображаются и доступны сразу
        self.find_element(LoginPageLocators.ENTRANCE_PANEL)
        self.find_element(LoginPageLocators.QR_CODE_PANEL)

        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)

        self.find_element(LoginPageLocators.LOGIN_BUTTON)

        self.find_element(LoginPageLocators.QA_GET)

        self.find_element(LoginPageLocators.NE_POLUCHAYETSYA_VOYTI_1)

        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_1)

        self.find_element(LoginPageLocators.VK_ENTRANCE)
        self.find_element(LoginPageLocators.MAIL_ENTRANCE)
        self.find_element(LoginPageLocators.YANDEX_ENTRANCE)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def random_text(self):
        # Генерация случайной строки (10 символов)
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return random_text

    def input_random_text_login_field(self):
        random_text = self.random_text()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(random_text)

