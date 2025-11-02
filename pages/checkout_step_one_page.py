from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from utils.logger import log


class CheckoutPageOne(BasePage):

    FIRST_NAME = (By.XPATH , '//input[@id="first-name"]')
    LAST_NAME = (By.XPATH , '//input[@id="last-name"]')
    ZIP_CODE = (By.XPATH , '//input[@id="postal-code"]')
    CONTINUE_BUTTON = (By.XPATH , '//input[@value="CONTINUE"]')
    CANCEL_BUTTON = (By.XPATH , '//a[text()="CANCEL"]')

    @allure.step("Проверить наличие текста 'Checkout: Your Information'")
    def checkout_your_information(self):
        locator = (By.XPATH, '//div[text()="Checkout: Your Information"]')
        return self.driver.find_element(*locator)
    log.info(f"Проверено наличие текста: 'Checkout: Your Information' на странице")

    @allure.step("Ввести first_name, last_name, zip_code и нажать кнопку 'CONTINUE'")
    def enter_information(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME, first_name)
        log.info(f"Введён текст в поле {first_name}")
        self.type(self.LAST_NAME, last_name)
        log.info(f"Введён текст в поле {last_name}")
        self.type(self.ZIP_CODE, zip_code)
        log.info(f"Заполнено поле {zip_code}")
        self.click(self.CONTINUE_BUTTON)
        log.info(f"Нажали кнопку 'CONTINUE'")
