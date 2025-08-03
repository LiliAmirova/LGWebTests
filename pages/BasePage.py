# пропишем, как будем искать элемент на странице
from selenium.webdriver.support.wait import WebDriverWait # ожидание появление состояние у элементов на странице
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5): # поиск элемента по локатору
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент{locator}")

    @allure.step('Открываем главную страницу')
    def get_url(self, url): #перехода по оперделенной url адресу, чтобы открывать нужные старницы
        return self.driver.get(url)

    def attach_screenshot(self): # прикрепление скриншота
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)