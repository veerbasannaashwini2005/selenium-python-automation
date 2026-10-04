from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Login
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
).send_keys("secret_sauce")

wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
).click()

# Wait for product
product = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "inventory_item_name")
    )
)

print("First Product:", product.text)

# Assertion
assert product.text == "Sauce Labs Backpack"

print("TEST PASSED")

driver.quit()