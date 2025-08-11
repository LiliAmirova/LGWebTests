
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random
import allure

class RegistrationPageLocators:
    PHONE_FIELD = (By.ID,'field_phone')
    COUNTRY_LIST = (By.XPATH,'//div[@data-l="t,country"]') # кнопка, которая открывает список стран
    COUNTRY_ITEM = (By.XPATH,'//div[@class="country-select_code"]') # видимость кнопки не сразу при открытии страницы
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]') # кнопка "Далее"
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]') # кнопка "Обраться в службу поддержки

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    @allure.step('Выбираем рандомную страну из списка')
    def select_random_county(self): # выбор рандомной страны
        random_numder = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM) # все элелементы, которые найдем положим в массив, возвращается списко веб-элементов
        country_code = country_items[random_numder].get_attribute('text')
        country_items[random_numder].click()
        self.attach_screenshot()
        return country_code


    @allure.step('Проверка на соответствие  кода телефона и выбранное рандомной страны')
    def get_phone_field_value(self): # функция возвращает код телефона
        self.attach_screenshot()
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('text')

