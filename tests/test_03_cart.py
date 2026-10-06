import time
from selenium.webdriver.common.by import By

def test_agregar_producto_al_carrito(driver):
    """Verifica que se pueda agregar 1 producto al carrito correctamente."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(1)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1


def test_agregar_multiples_productos_al_carrito(driver):
    """Verifica que se puedan agregar 2 productos al carrito correctamente."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(1)
    # Clic en el primer producto
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    
    # Clic en el segundo producto (buscado directamente al momento de hacer clic)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(1)
    
    # Validar badge igual a 2
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "2"
    
    # Ir al carrito y validar que existan 2 ítems
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2