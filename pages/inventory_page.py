from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from utils.logger import log


class InventoryPage(BasePage):
    """Страница каталога товаров"""

    ADD_TO_CART_BUTTON = (By.XPATH, '//button[text()="ADD TO CART"]') # кнопка добавить товар
    REMOVE_BUTTON = (By.XPATH, '//button[text()="REMOVE"]') # кнопка удалить товар из корзины
    SORTING = (By.XPATH, '//*[@class="product_sort_container"]') # кнопка открывающая список сортировки
    ALL_PRODUCTS = (By.XPATH, '//*[@class="inventory_item"]') # все товары имеют
    PRODUCT_NAME = (By.XPATH, '//*[@class="inventory_item_name"]') # у каждого товара свой текст названия
    CART_COUNTER = (By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')

    @allure.step("Открыть страницу каталога товаров")
    def open_inventory_page(self):
        """Открывает страницу каталога"""
        self.open("https://www.saucedemo.com/v1/inventory.html")
        log.info(f"Открыли страницу каталога")

    def get_all_products(self):
        locator = (By.XPATH, '//div[@class="inventory_item"]')
        return self.driver.find_elements(*locator)
    log.info(f"Получили список всех подуктов на странице")

    def find_product_by_name(self, product_name):
        """Находит элемент товара по имени"""
        locator = (By.XPATH, f'//div[@class="inventory_item_name" and text()="{product_name}"]')
        log.info(f"Нашли товар {product_name} по названию")
        return self.driver.find_element(*locator)

    def press_button_add_cart_by_product_name(self, product_name):
        """Находит кнопку добавления в корзину для конкретного товара"""
        locator = (By.XPATH, f'//div[text()="{product_name}"]/following::button[text()="ADD TO CART"]')
        log.info(f"Нашли кнопку добавления товара {product_name} по названию товара")
        return self.driver.find_element(*locator)

    def press_button_remove_from_cart(self, product_name):
        """Находит кнопку удаления из корзины конкретного товара"""
        locator = (By.XPATH, f'//div[text()="{product_name}"]/following::button[text()="REMOVE"]')
        log.info(f"Нашли кнопку удаления товара {product_name} по названию товара")
        return self.driver.find_element(*locator)

    @allure.step("Добавить товар по названию в корзину")
    def add_to_cart(self, product_name):
        """Добавляет товар в корзину по имени"""
        product = self.find_product_by_name(product_name)
        press_button = self.press_button_add_cart_by_product_name(product_name)
        press_button.click()
        log.info(f"Нашли и добавили в корзину товар {product_name} по названию товара")

    @allure.step("Удалить товар по названию из корзины")
    def remove_from_cart(self, product_name):
        """Удаляет выбранный товар из корзины"""
        product = self.find_product_by_name(product_name)
        press_button = self.press_button_remove_from_cart(product_name)
        press_button.click()
        log.info(f"Нашли и удалили из корзины товар {product_name} по названию товара")

    def select_sort_dropdown(self):
        """Выбирает сортировку через dropdown"""
        self.wait.until(EC.presence_of_element_located(self.SORTING))
        return self.driver.find_element(*self.SORTING)
    log.info(f"Нашли и открыли dropdown для дальнейшей сортировки товаров")

    def find_sort_element_by_name(self, sort_name):
        """Находит элемент сортировки по названию"""
        locator = (By.XPATH, f'//option[text()="{sort_name}"]')
        log.info(f"Нашли сортировку {sort_name} по названию сортировки")
        return self.driver.find_element(*locator)

    @allure.step("Выбрать сортировку товара по названию сортировки")
    def select_sort_products(self, sort_name):
        self.select_sort_dropdown().click()
        self.click(self.find_sort_element_by_name(sort_name))
        log.info(f"Применили сортировку {sort_name} по названию сортировки")

    def get_all_product_names(self):
        products_list = self.get_all_products()
        names = []
        for product in products_list:
            name_element = product.find_element(*self.PRODUCT_NAME)
            names.append(name_element.text.strip())
        return names

    def get_all_product_prices(self):
        """Возвращает список цен всех товаров (числами)"""
        products_list = self.get_all_products()
        prices = []
        for product in products_list:
            price_element = product.find_element(*self.PRODUCT_PRICE)
            price_text = price_element.text.replace('$', '').strip()
            prices.append(float(price_text))
        return prices

    @allure.step("Проверить сортировку по названию сортировки")
    def is_sorted_correctly(self, sort_name):
        """Универсальная проверка сортировки по названию"""
        if sort_name == 'Name (A to Z)':
            log.info(f"Применили сортировку {sort_name}")
            names = self.get_all_product_names()
            return names == sorted(names, key=str.lower)

        elif sort_name == 'Name (Z to A)':
            log.info(f"Применили сортировку {sort_name}")
            names = self.get_all_product_names()
            return names == sorted(names, key=str.lower, reverse=True)

        elif sort_name == 'Price (low to high)':
            log.info(f"Применили сортировку {sort_name}")
            prices = self.get_all_product_prices()
            return prices == sorted(prices)

        elif sort_name == 'Price (high to low)':
            log.info(f"Применили сортировку {sort_name}")
            prices = self.get_all_product_prices()
            return prices == sorted(prices, reverse=True)

        # Для неизвестных типов сортировки просто возвращаем False
        return False


