from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import get_logger


logger = get_logger(__name__)


def test_stale_element_retry(driver):

    logger.info("Stale element test started")

    driver.get("https://the-internet.herokuapp.com/dynamic_content")

    wait = WebDriverWait(driver, 10)

    def get_text_with_retry(driver):
        try:
            element = driver.find_element(
                By.CSS_SELECTOR,
                ".large-10.columns"
            )

            return element.text

        except StaleElementReferenceException:
            logger.warning("Stale element detected. Retrying...")
            return False

    text = wait.until(get_text_with_retry)

    assert text != ""

    logger.info("Element found successfully")
    logger.info("Stale element test passed")

    print("STALE ELEMENT RETRY TEST PASSED")