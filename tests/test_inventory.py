from conftest import *
import pytest
from pages.inventory_page import InventoryPage
from pages.header import Header
from pages.login_page import LoginPage



@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_to_cart(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.open_inventory_page()
    header = Header(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    assert header.cart_counter() == 2

@pytest.mark.ui
@pytest.mark.smoke
def test_remove_product_from_cart(driver):
    inventory_page = InventoryPage(driver)
    header = Header(driver)
    inventory_page.open_inventory_page()
    inventory_page.add_to_cart('Test.allTheThings() T-Shirt (Red)')
    inventory_page.remove_from_cart('Test.allTheThings() T-Shirt (Red)')
    assert header.cart_counter() == 0

@pytest.mark.ui
def test_sorting_products(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.open_inventory_page()
    inventory_page.select_sort_products('Name (Z to A)')
    assert inventory_page.is_sorted_correctly('Name (Z to A)')











