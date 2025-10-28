from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


class Header(BasePage):
    CART_BUTTON = (By.XPATH, '//*[@class="shopping_cart_link fa-layers fa-fw"]')  # кнопка корзины
    CART_COUNTER = (By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]') # счётчик корзины
    OPEN_MENU_BUTTON = (By.XPATH, '//button[text()="Open Menu"]') # открыть боковое меню
    INVENTORY_PAGE_BUTTON = (By.XPATH, '//a[@id="inventory_sidebar_link"]') # перейти в каталог
    ABOUT_BUTTON = (By.XPATH, '//a[text()="About"]') # ошибка "403 Forbidden"
    LOGOUT_BUTTON = (By.XPATH, '//a[text()="Logout"]') # выйти из аккаунта
    RESET_APP_STATE_BUTTON = (By.XPATH, '//a[text()="Reset App State"]') # сбросить все действия

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Кнопка перехода в корзину"""
        self.click(self.CART_BUTTON)

    def cart_counter_is_displayed(self):
        """Проверяет, отображается ли счетчик корзины"""
        try:
            counter = self.driver.find_element(*self.CART_COUNTER)
            return counter.is_displayed()
        except:
            return False

    @allure.step("Проверить чему равен счётчик корзины")
    def cart_counter(self):
        """Возвращает количество товаров или 0 если счетчика нет"""
        if self.cart_counter_is_displayed():
            count_text = self.get_text(self.CART_COUNTER)
            return int(count_text)
        return 0

    @allure.step("Открыть боковое меню")
    def open_menu(self):
        """Открыть боковое меню"""
        self.click(self.OPEN_MENU_BUTTON)

    @allure.step("Вернуться в каталог")
    def press_inventory_page_button(self):
        """Кнопка возврата в каталог"""
        self.click(self.INVENTORY_PAGE_BUTTON)

    @allure.step("403 Forbidden")
    def press_about_button(self):
        self.click(self.ABOUT_BUTTON)

    @allure.step("Выйти из аккаунта")
    def press_logout_button(self):
        """Кнопка выхода из аккаунта"""
        self.click(self.LOGOUT_BUTTON)

    @allure.step("Рестарт страницы")
    def press_reset_app_state_button(self):
        """Кнопка рестарта на странице"""
        self.click(self.RESET_APP_STATE_BUTTON)