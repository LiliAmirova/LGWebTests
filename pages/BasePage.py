# пропишем, как будем искать элемент на странице
from selenium.webdriver.support.wait import WebDriverWait # ожидание появление состояние у элементов на странице
from selenium.webdriver.support import expected_conditions
import allure



class BasePage:
    def __init__(self, driver):
        self.driver = driver

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





