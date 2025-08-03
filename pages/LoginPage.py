from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTRANCE_PANEL = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE_PANEL = (By.XPATH, '//*[@data-l="t,qr_tab"]')

    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')

    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')

    QA_GET = (By.XPATH, '//*[@data-l="t, get_qr"]')

    # Какой из вариантов  ниже лучше использовать ?
    NE_POLUCHAYETSYA_VOYTI_1 = (By.XPATH, '//*[@class="lp"]')
    NE_POLUCHAYETSYA_VOYTI_2 = (By.XPATH, '//div[@class="recovery-link"]/a[@data-l="t,register"]')

    # Какой из вариантов  ниже лучше использовать ?
    REGISTRATION_BUTTON_1 = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]' )
    REGISTRATION_BUTTON_2 = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')

    VK_ENTRANCE = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_ENTRANCE = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_ENTRANCE = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass

