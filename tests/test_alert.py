from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click "Click for JS Alert"
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Alert']"
    ).click()

    # Wait for alert
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    # Get alert message
    alert_text = alert.text

    assert alert_text == "I am a JS Alert"

    # Accept alert
    alert.accept()

    print("ALERT TEST PASSED")