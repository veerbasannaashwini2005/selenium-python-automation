from selenium.webdriver.common.by import By


def test_radio_button(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    radio_buttons = driver.find_elements(
        By.CSS_SELECTOR, "input[type='radio']"
    )

    # Select the first radio button
    if not radio_buttons[0].is_selected():
        radio_buttons[0].click()

    assert radio_buttons[0].is_selected()

    print("RADIO BUTTON TEST PASSED")