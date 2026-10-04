from selenium.webdriver.common.by import By


class ProductsPage:

    BACKPACK = (
        By.XPATH,
        "//div[contains(@class,'inventory_item')][.//div[text()='Sauce Labs Backpack']]//button"
    )

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.BACKPACK).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()