from selenium.webdriver.common.action_chains import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    PROFILE_ACCESS = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAYED_FUNCTIONS = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES_AND_APPS =(By.XPATH, '//a[contains(@href, "igry-i-prilojeniya")]')
    OTHER_SERVICES = (By.XPATH, '//a[contains(@href, "drugie-servisy")]')
    IMPORTANT_INFORMATION = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISEMENT_CABINET  = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self): # функция, которая проверяет страницу на наличие и видимость элементов по локаторам, которые отображаются и доступны сразу
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()

        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

    @allure.step('Скроллим до искомого элемента и кликаем на него')
    def scrollToitem(self, locator):
        try:
            # 1. Явное ожидание элемента
            scroll_item = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            # 2. Скролл к элементу с дополнительным смещением (если нужно)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", scroll_item)

            # 3. Небольшая пауза для стабилизации
            time.sleep(0.5)

            # 4. Повторно находим элемент (на случай stale reference)
            scroll_item = self.driver.find_element(*locator)
            self.attach_screenshot()

            # 5. Делаем скриншот
            self.attach_element_screenshot(scroll_item, "Скриншот элемента перед кликом")

            # 6. Действия с элементом
            ActionChains(self.driver).move_to_element(scroll_item).click().perform()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), "Ошибка при скролле", allure.attachment_type.PNG)
            raise e


