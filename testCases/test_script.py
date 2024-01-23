# test_script.py
import pytest
from Saucedemo_new_Approach2_E2E_test.pages.login_page import LoginPage
from Saucedemo_new_Approach2_E2E_test.pages.plp_page import PLPPage
from Saucedemo_new_Approach2_E2E_test.pages.pdp_page import PDPPage
from Saucedemo_new_Approach2_E2E_test.pages.cart_page import CartPage
from Saucedemo_new_Approach2_E2E_test.pages.checkout_page import CheckoutPage
from Saucedemo_new_Approach2_E2E_test.pages.confirmation_page import ConfirmationPage
from Saucedemo_new_Approach2_E2E_test.pages.completion_page import CompletionPage
from Saucedemo_new_Approach2_E2E_test.pages.logout_page import Logout
from Saucedemo_new_Approach2_E2E_test.config.config_file import TestData


# Using pytest.mark.usefixtures to set up the test environment
@pytest.mark.usefixtures("setup")
class TestEndToEnd:
    # Test case for the end-to-end flow
    def test_end_to_end_flow(self):
        # Instantiate LoginPage class
        login_page = LoginPage(self.driver)
        # Open the login page
        login_page.open()
        # Log in using test data
        login_page.login(TestData.username, TestData.password)
        # Instantiate PLPPage class
        plp_page = PLPPage(self.driver)
        # Select products on the Product List Page (PLP) using test data
        product_names = TestData.list_of_product_names
        plp_page.select_product(product_names)
        # Instantiate PDPPage class
        pdp_page = PDPPage(self.driver)
        # Add a product to the cart on the Product Detail Page (PDP)
        pdp_page.add_to_cart()
        # Instantiate CartPage class
        cart_page = CartPage(self.driver)
        # Remove all or selected products from the cart or Navigate to the checkout page from the cart
        # cart_page.remove_selected_products_from_cart(["Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"])
        # cart_page.remove_all_products_from_cart()
        cart_page.navigate_to_checkout()
        # Instantiate CheckoutPage class
        checkout_page = CheckoutPage(self.driver)
        # Enter shipping information on the checkout page using test data
        checkout_page.enter_shipping_info(TestData.first_name, TestData.last_name, TestData.zip_code)
        # Instantiate ConfirmationPage class
        confirmation_page = ConfirmationPage(self.driver)
        # Complete the checkout process on the confirmation page
        confirmation_page.complete_checkout()
        # Instantiate CompletionPage class
        completion_page = CompletionPage(self.driver)
        # Navigate back to the home page from the completion page
        completion_page.back_to_home()
        # Instantiate Logout class
        home_page = Logout(self.driver)
        # Log out from the application
        home_page.logout()

