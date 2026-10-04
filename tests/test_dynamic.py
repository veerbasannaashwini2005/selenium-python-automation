from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_element(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Remove']")
        )
    )

    remove_button.click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert "It's gone!" in message.text

    print("DYNAMIC ELEMENT TEST PASSED")