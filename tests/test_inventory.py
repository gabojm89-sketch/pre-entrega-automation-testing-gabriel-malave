from selenium.webdriver.common.by import By

def test_verificacion_catalogo(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0
    
    first_item_name = items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_item_price = items[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    assert first_item_name != ""
    assert "$" in first_item_price