from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from utils.logger import log


class CheckoutPageComplete(BasePage):

    COMPLETE_HEADER = (By.XPATH, '//*[text()="THANK YOU FOR YOUR ORDER"]')

    @allure.step("Проверить наличие текста 'THANK YOU FOR YOUR ORDER'")
    def complete_header(self):
        locator = (By.XPATH, '//*[text()="THANK YOU FOR YOUR ORDER"]')
        return self.driver.find_element(*locator)
    log.info(f"Проверено наличие текста: 'THANK YOU FOR YOUR ORDER' на странице")
