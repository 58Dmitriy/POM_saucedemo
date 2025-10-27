from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class CartPage(BasePage):
    """Страница корзины товаров"""

    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//a[@class="btn_secondary"]') # кнопка вернуться в каталог товаров
    CHECKOUT_BUTTON = (By.XPATH, '//a[contains(@class,"checkout_button")]') # кнопка подтвердить заказ
    CART_LIST = (By.XPATH, '//div[@class="cart_list"]') # лист корзины
    REMOVE_BUTTON = (By.XPATH, '//button[contains(@class,"cart_button") and text()="REMOVE"]')

    def waiting_for_cart_list(self):
        """Ожидает и находит элемент CART_LIST на странице"""
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))
        return self.driver.find_element(*self.CART_LIST)

    def waiting_for_items_in_the_cart(self, product_name):
        """Находит товар в корзине по названию"""
        locator = (By.XPATH, f'//div[@class="inventory_item_name" and text()="{product_name}"]')
        return self.driver.find_element(*locator)

    def press_remove_button(self, product_name):
        locator = (By.XPATH, f'//div[text()="{product_name}"]/following::button[text()="REMOVE"]')
        return self.driver.find_element(*locator)

    def remove_product(self, product_name):
        """Удаление товара по названию"""
        self.waiting_for_items_in_the_cart(product_name)
        self.press_remove_button(product_name).click()

    def press_checkout_button(self):
        """Нажать на кнопку checkout"""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def checkout_your_information(self):
        locator = (By.XPATH, '//div[text()="Checkout: Your Information"]')
        return self.driver.find_element(*locator)



