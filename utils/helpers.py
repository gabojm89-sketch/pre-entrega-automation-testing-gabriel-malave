import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    """Inicializa y cierra Chrome WebDriver antes y después de cada test."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def wait_for_element(driver, by_type, locator, timeout=10):
    """Espera explícita hasta que un elemento sea visible."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by_type, locator))
    )