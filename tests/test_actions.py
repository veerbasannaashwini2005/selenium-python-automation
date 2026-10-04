from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mouse_actions(driver):
    driver.get("https://the-internet.herokuapp.com/context_menu")

    box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "hot-spot"))
    )

    actions = ActionChains(driver)

    # Right-click
    actions.context_click(box).perform()

    # Verify JavaScript alert
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    assert "You selected a context menu" in alert.text

    alert.accept()

    print("MOUSE ACTION TEST PASSED")