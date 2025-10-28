from conftest import *
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_step_one_page import CheckoutPageOne
from pages.checkout_step_two_page import CheckoutPageTwo
from pages.checkout_complete_page import CheckoutPageComplete
from pages.header import Header


@pytest.mark.ui
def test_cart_checkout(driver):
    cart_page = CartPage(driver)
    inventory_page = InventoryPage(driver)
    header = Header(driver)
    checkout_page_one = CheckoutPageOne(driver)

    inventory_page.open_inventory_page()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    header.go_to_cart()
    assert cart_page.waiting_for_cart_list()
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Backpack")
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Bolt T-Shirt")
    cart_page.remove_product("Sauce Labs Backpack")
    assert header.cart_counter() == 1
    cart_page.press_checkout_button()
    assert checkout_page_one.checkout_your_information()

@pytest.mark.ui
@pytest.mark.smoke
def test_full_cart_checkout(driver):
    cart_page = CartPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page_one = CheckoutPageOne(driver)
    checkout_page_two = CheckoutPageTwo(driver)
    checkout_page_complete = CheckoutPageComplete(driver)
    header = Header(driver)

    inventory_page.open_inventory_page()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    header.go_to_cart()
    assert cart_page.waiting_for_cart_list()
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Backpack")
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Bolt T-Shirt")
    cart_page.remove_product("Sauce Labs Backpack")
    assert header.cart_counter() == 1
    cart_page.press_checkout_button()
    assert checkout_page_one.checkout_your_information()
    checkout_page_one.enter_information("test", "test_test", 123456)
    assert checkout_page_two.checkout_overview()
    assert cart_page.waiting_for_items_in_the_cart("Sauce Labs Bolt T-Shirt")
    checkout_page_two.press_finish_button()
    assert checkout_page_complete.complete_header()



