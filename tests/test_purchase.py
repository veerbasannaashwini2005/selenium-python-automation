from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_backpack_to_cart(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("inventory.html")
    )

    # Products page
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    # Open cart
    products_page.open_cart()

    wait.until(
        EC.url_contains("cart.html")
    )

    # Cart page
    cart_page = CartPage(driver)

    product_name = cart_page.get_product_name()

    assert product_name == "Sauce Labs Backpack"

    print("ADD TO CART TEST PASSED")