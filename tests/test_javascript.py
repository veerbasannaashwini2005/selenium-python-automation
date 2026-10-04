from selenium.webdriver.common.by import By


def test_javascript_executor(driver):
    driver.get("https://www.saucedemo.com/")

    # Find username field
    username = driver.find_element(By.ID, "user-name")

    # Enter text using JavaScript
    driver.execute_script(
        "arguments[0].value = 'standard_user';",
        username
    )

    # Read the value
    value = driver.execute_script(
        "return arguments[0].value;",
        username
    )

    assert value == "standard_user"

    print("JAVASCRIPT EXECUTOR TEST PASSED")