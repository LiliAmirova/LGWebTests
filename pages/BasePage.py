# пропишем, как будем искать элемент на странице
from operator import index

from selenium.webdriver.support.wait import WebDriverWait # ожидание появление состояние у элементов на странице
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure
import time


class BasePageLocators:
    LOGO_BUTTON = (By.ID, 'nohook_logo_link')
    VK_ECOSYSTEM_BUTTON = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver


    def check_page(self): # функция, которая проверяет страницу на наличие и видимость элементов по локаторам, которые отображаются и доступны сразу
        with allure.step('Проверяем наличие кнопок на странице'):
            self.attach_screenshot()

            self.find_element(BasePageLocators.LOGO_BUTTON)
            self.attach_element_screenshot_locator(BasePageLocators.LOGO_BUTTON, 'Проверяем наличие кнопки Логотипа')

            self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON)
            self.attach_element_screenshot_locator(BasePageLocators.VK_ECOSYSTEM_BUTTON, 'Проверяем наличие кнопки Экосистемы')



    def find_element(self, locator, time=5): # поиск элемента по локатору
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент{locator}")


    def find_elements(self, locator, time=5): # поиск элементы из выпадающего списка по локатору
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f"Не удалось найти элементы{locator}")


    @allure.step('Открываем главную страницу')
    def get_url(self, url): #перехода по оперделенной url адресу, чтобы открывать нужные старницы
        return self.driver.get(url)


    def attach_screenshot(self): # прикрепление скриншота
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)


    def attach_element_screenshot(self, element, name):
        allure.attach(
            element.screenshot_as_png,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def attach_element_screenshot_locator(self, locator, name):
        element = self.driver.find_element(*locator)  # Находим элемент по локатору
        allure.attach(
            element.screenshot_as_png,  # Теперь element — это WebElement
            name=name,
            attachment_type=allure.attachment_type.PNG
        )


    @allure.step('Нажимаем на кнопку Экосистемы')
    def click_vk_ecosystem(self):
        self.attach_element_screenshot_locator(BasePageLocators.VK_ECOSYSTEM_BUTTON, "скрин кнопки Экосистемы")
        self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON).click()


    @allure.step('Нажимаем на кнопку Еще')
    def click_more_button(self):
        self.attach_element_screenshot_locator(BasePageLocators.MORE_BUTTON, 'скрин кнопки "Eще"')
        self.find_element(BasePageLocators.MORE_BUTTON).click()


    def get_windows_id(self, index): # индекс вкладки
        return self.driver.window_handles[index]


    @allure.step('Переходим с одной вкладки на другую')
    def switch_window(self, window_id):
        self.attach_screenshot()
        self.driver.switch_to.window(window_id)
        self.attach_screenshot()







