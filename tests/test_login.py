import json

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config import TIMEOUT


with open("test_data/login_data.json", "r") as file:
    login_data = json.load(file)


@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("data", login_data)
def test_login(driver, data):

    login_page = LoginPage(driver)

    login_page.login(
        data["username"],
        data["password"]
    )

    wait = WebDriverWait(driver, TIMEOUT)

    if data["expected_success"]:

        wait.until(
            EC.url_contains("inventory.html")
        )

        assert "inventory.html" in driver.current_url

    else:

        error = wait.until(
            EC.visibility_of_element_located(
                login_page.ERROR_MESSAGE
            )
        )

        assert error.is_displayed()