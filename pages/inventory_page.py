from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    """Страница каталога товаров"""

    CART_BUTTON = (By.XPATH, '//*[@class="shopping_cart_link fa-layers fa-fw"]') # кнопка корзины
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[text()="ADD TO CART"]') # кнопка добавить товар
    REMOVE_BUTTON = (By.XPATH, '//button[text()="REMOVE"]') # кнопка удалить товар из корзины
    SORTING = (By.XPATH, '//*[@class="product_sort_container"]') # кнопка открывающая список сортировки
    ALL_PRODUCTS = (By.XPATH, '//*[@class="inventory_item"]') # все товары имеют
    PRODUCT_NAME = (By.XPATH, '//*[@class="inventory_item_name"]') # у каждого товара свой текст названия
    CART_COUNTER = (By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')

    def open_inventory_page(self):
        """Открывает страницу каталога"""
        self.open("https://www.saucedemo.com/v1/inventory.html")

    def go_to_cart(self):
        """Кнопка перехода в корзину"""
        self.click(self.CART_BUTTON)

    def get_all_products(self):
        locator = (By.XPATH, '//div[@class="inventory_item"]')
        return self.driver.find_elements(*locator)

    def find_product_by_name(self, product_name):
        """Находит элемент товара по имени"""
        locator = (By.XPATH, f'//div[@class="inventory_item_name" and text()="{product_name}"]')
        return self.driver.find_element(*locator)

    def press_button_add_cart_by_product_name(self, product_name):
        """Находит кнопку добавления в корзину для конкретного товара"""
        locator = (By.XPATH, f'//div[text()="{product_name}"]/following::button[text()="ADD TO CART"]')
        return self.driver.find_element(*locator)

    def press_button_remove_from_cart(self, product_name):
        """Находит кнопку удаления из корзины конкретного товара"""
        locator = (By.XPATH, f'//div[text()="{product_name}"]/following::button[text()="REMOVE"]')
        return self.driver.find_element(*locator)

    def cart_counter_is_displayed(self):
        """Проверяет, отображается ли счетчик корзины"""
        try:
            counter = self.driver.find_element(*self.CART_COUNTER)
            return counter.is_displayed()
        except:
            return False

    def cart_counter(self):
        """Возвращает количество товаров или 0 если счетчика нет"""
        if self.cart_counter_is_displayed():
            count_text = self.get_text(self.CART_COUNTER)
            return int(count_text)
        return 0

    def add_to_cart(self, product_name):
        """Добавляет товар в корзину по имени"""
        product = self.find_product_by_name(product_name)
        press_button = self.press_button_add_cart_by_product_name(product_name)
        press_button.click()

    def remove_from_cart(self, product_name):
        """Удаляет выбранный товар из корзины"""
        product = self.find_product_by_name(product_name)
        press_button = self.press_button_remove_from_cart(product_name)
        press_button.click()

    def select_sort_dropdown(self):
        """Выбирает сортировку через dropdown"""
        self.wait.until(EC.presence_of_element_located(self.SORTING))
        return self.driver.find_element(*self.SORTING)

    def find_sort_element_by_name(self, sort_name):
        """Находит элемент сортировки по названию"""
        locator = (By.XPATH, f'//option[text()="{sort_name}"]')
        return self.driver.find_element(*locator)

    def select_sort_products(self, sort_name):
        self.select_sort_dropdown().click()
        self.find_sort_element_by_name(sort_name).click()

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

    def is_sorted_correctly(self, sort_name):
        """Универсальная проверка сортировки по названию"""
        if sort_name == 'Name (A to Z)':
            names = self.get_all_product_names()
            return names == sorted(names, key=str.lower)

        elif sort_name == 'Name (Z to A)':
            names = self.get_all_product_names()
            return names == sorted(names, key=str.lower, reverse=True)

        elif sort_name == 'Price (low to high)':
            prices = self.get_all_product_prices()
            return prices == sorted(prices)

        elif sort_name == 'Price (high to low)':
            prices = self.get_all_product_prices()
            return prices == sorted(prices, reverse=True)

        # Для неизвестных типов сортировки просто возвращаем False
        return False


