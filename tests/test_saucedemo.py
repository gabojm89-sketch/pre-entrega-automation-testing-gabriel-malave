import pytest
from selenium.webdriver.common.by import By
from utils.helpers import driver, wait_for_element

BASE_URL = "https://www.saucedemo.com/"

# --- CASO 1: LOGIN ---
def test_login_exitoso(driver):
    driver.get(BASE_URL)
    
    username_field = wait_for_element(driver, By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    assert "/inventory.html" in driver.current_url, "URL no coincide tras el login."
    header_title = wait_for_element(driver, By.CLASS_NAME, "title").text
    assert header_title == "Products", f"Título esperado 'Products', pero se obtuvo '{header_title}'"

# --- CASO 2: CATÁLOGO DE PRODUCTOS ---
def test_verificacion_catalogo(driver):
    driver.get(BASE_URL)
    wait_for_element(driver, By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(inventory_items) > 0, "No se encontraron productos."
    
    first_item_name = inventory_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_item_price = inventory_items[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n[INFO] Producto: '{first_item_name}' - Precio: {first_item_price}")

# --- CASO 3: CARRITO DE COMPRAS ---
def test_agregar_producto_al_carrito(driver):
    driver.get(BASE_URL)
    wait_for_element(driver, By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    first_item = wait_for_element(driver, By.CLASS_NAME, "inventory_item")
    product_name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    first_item.find_element(By.TAG_NAME, "button").click()
    
    cart_badge = wait_for_element(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "El contador del carrito debería mostrar 1"
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver.current_url
    
    item_in_cart = wait_for_element(driver, By.CLASS_NAME, "inventory_item_name").text
    assert item_in_cart == product_name