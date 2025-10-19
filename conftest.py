import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    options = Options()
    # options.add_argument('--headless')
    options.add_argument("--start-maximized")
    prefs = {
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()