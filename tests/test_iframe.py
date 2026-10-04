from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iframe(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")

    # Switch into iframe
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )

    driver.switch_to.frame(iframe)

    # Find editor
    editor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tinymce"))
    )

    # Use JavaScript to enter text
    driver.execute_script(
        "arguments[0].innerHTML = 'Selenium iframe testing';",
        editor
    )

    # Verify text
    assert editor.text == "Selenium iframe testing"

    print("IFRAME TEST PASSED")

    # Return to main page
    driver.switch_to.default_content()