from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from utils.logger import log

class CheckoutPageTwo(BasePage):
    FINISH_BUTTON = (By.XPATH, '//a[text()="FINISH"]')

    @allure.step("Проверить наличие текста 'Checkout: Overview'")
    def checkout_overview(self):
        locator = (By.XPATH, '//div[text()="Checkout: Overview"]')
        return self.driver.find_element(*locator)
    log.info(f"Проверено наличие текста: 'Checkout: Overview' на странице")

    @allure.step("Нажать на кнопку 'Finish'")
    def press_finish_button(self):
        """Нажать на кнопку Finish"""
        self.click(self.FINISH_BUTTON)
        log.info(f"Нажали кнопку 'FINISH'")