import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import BASE_URL


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    driver.get(BASE_URL)

    yield driver

    driver.quit()