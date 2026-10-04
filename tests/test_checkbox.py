from selenium.webdriver.common.by import By


def test_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # Checkbox 1
    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    assert checkboxes[0].is_selected()

    print("CHECKBOX TEST PASSED")