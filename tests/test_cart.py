from conftest import *
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
import time

def test_cart_checkout(driver):
    cart_page = CartPage(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.open_inventory_page()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.go_to_cart()
    assert cart_page.waiting_for_cart_list()
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Backpack")
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Bolt T-Shirt")
    cart_page.remove_product("Sauce Labs Backpack")
    assert inventory_page.cart_counter() == 1
    cart_page.press_checkout_button()
    assert cart_page.checkout_your_information()

