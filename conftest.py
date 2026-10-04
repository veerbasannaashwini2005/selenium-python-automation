import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config import BASE_URL


@pytest.fixture
def driver():
    driver_path = Path(__file__).resolve().parent / "drivers" / "chromedriver.exe"

    service = Service(str(driver_path))
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()