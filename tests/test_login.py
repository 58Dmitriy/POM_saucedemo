import conftest
import pytest
from pages.login_page import LoginPage
from utils.logger import log


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    log.info("Старт теста: test_successful_login")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    log.info("Тест (test_successful_login) успешно завершён")


@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(driver):
    log.info("Старт теста: test_invalid_login")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("invalid", "invalid")
    assert "Epic sadfac" in login_page.get_error_message()
    log.info("Тест (test_invalid_login) успешно завершён")


