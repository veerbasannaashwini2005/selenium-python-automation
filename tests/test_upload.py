import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_file_upload(driver):

    driver.get("https://the-internet.herokuapp.com/upload")

    # Create a test file
    file_path = os.path.abspath("test_upload.txt")

    with open(file_path, "w") as file:
        file.write("This is a Selenium file upload test.")

    # Find file input
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "file-upload")
        )
    )

    # Upload file
    upload_input.send_keys(file_path)

    # Click Upload
    driver.find_element(By.ID, "file-submit").click()

    # Verify upload
    uploaded_file = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "uploaded-files")
        )
    )

    assert uploaded_file.text == "test_upload.txt"

    print("FILE UPLOAD TEST PASSED")

    # Delete test file
    os.remove(file_path)
    