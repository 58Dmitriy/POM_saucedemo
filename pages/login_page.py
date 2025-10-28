from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


class LoginPage(BasePage):
    """Страница логина"""

    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open("https://www.saucedemo.com/v1/index.html")

    @allure.step("Ввести username, password и нажать кнопку 'LOGIN'")
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Проверить текст сообщения об ошибке")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)