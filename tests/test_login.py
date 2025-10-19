import conftest
import pytest
from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("invalid", "invalid")

    assert "Epic sadfac" in login_page.get_error_message()