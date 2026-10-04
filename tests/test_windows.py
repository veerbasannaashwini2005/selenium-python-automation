from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_windows(driver):
    driver.get("https://the-internet.herokuapp.com/windows")

    # Save the original window
    original_window = driver.current_window_handle

    # Click the link that opens a new window
    driver.find_element(
        By.LINK_TEXT, "Click Here"
    ).click()

    # Wait until a second window opens
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )

    # Get all windows
    windows = driver.window_handles

    # Switch to the new window
    for window in windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # Verify new window
    assert "New Window" in driver.find_element(By.TAG_NAME, "h3").text

    print("NEW WINDOW TEST PASSED")

    # Switch back to original window
    driver.switch_to.window(original_window)

    assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text