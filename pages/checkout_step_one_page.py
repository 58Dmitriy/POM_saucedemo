from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


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

    @allure.step("Ввести first_name, last_name, zip_code и нажать кнопку 'CONTINUE'")
    def enter_information(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)
