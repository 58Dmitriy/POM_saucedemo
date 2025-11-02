from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from utils.logger import log


class BasePage:
    """Базовый класс для всех страниц"""
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)
        log.info(f"Создан экземпляр страницы: {self.__class__.__name__}")

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)
        log.info(f"Открытие URL: {url}")

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        log.info(f"Клик по элементу с локатором: {locator}")

    @allure.step("Ввод текста '{text}'")
    def type(self, locator, text):
        log.info(f"Ввод текста '{text}' в элемент с локатором {locator}")
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        text = self.wait.until(EC.presence_of_element_located(locator))
        log.info(f"Текст элемента: '{text}'")
        return text

