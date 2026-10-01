from selenium.webdriver.common.by import By

def test_agregar_producto_al_carrito(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1