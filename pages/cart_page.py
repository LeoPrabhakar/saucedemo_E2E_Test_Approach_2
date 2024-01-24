# cart_page.py

# Import necessary modules from the Selenium library
import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import custom modules from the Saucedemo_new_Approach2_E2E_test package
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage
from Saucedemo_new_Approach2_E2E_test.config.config_file import TestData


# Define the CartPage class that inherits from the BasePage class
class CartPage(BasePage):

    # Define class variables for locators
    CART_PRODUCTS_LOCATOR = (By.XPATH, '//div[@class="cart_list"]//div//div//a//div')
    CHECKOUT_BUTTON_LOCATOR = (By.XPATH, "//button[@id='checkout']")
    REMOVE_BUTTON_LOCATOR = '//button[@class="btn btn_secondary btn_small cart_button"]'

    # Constructor to initialize the CartPage object
    def __init__(self, driver):
        super().__init__(driver)

    # Method to wait for a single element to be present in the DOM
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Method to wait for multiple elements to be present in the DOM
    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # Method to navigate to the checkout page
    def navigate_to_checkout(self):
        # Retrieve cart products and their names
        cart_products = self.wait_for_elements(self.CART_PRODUCTS_LOCATOR)
        cart_product_names = [product.text for product in cart_products]
        expected_product_names = TestData.list_of_product_names
        assert cart_product_names == expected_product_names, "Products in the cart do not match the expected list"
        print("Products added to the cart successfully!")

        # Click the checkout button
        checkout_btn = self.wait_for_element(self.CHECKOUT_BUTTON_LOCATOR)
        checkout_btn.click()

    # Method to remove selected products from the cart
    def remove_selected_products_from_cart(self, products_to_remove):
        cart_products = self.wait_for_elements(self.CART_PRODUCTS_LOCATOR)
        for selected_product in products_to_remove:
            product_removed = False

            while not product_removed:
                for cart_product in cart_products:
                    try:
                        if selected_product in cart_product.text:
                            remove_button = cart_product.find_element(By.XPATH, self.REMOVE_BUTTON_LOCATOR)
                            remove_button.click()
                            product_removed = True
                    except StaleElementReferenceException:
                        cart_products = self.wait_for_elements(self.CART_PRODUCTS_LOCATOR)

        time.sleep(3)
        checkout_btn = self.wait_for_element(self.CHECKOUT_BUTTON_LOCATOR)
        checkout_btn.click()

    # Method to remove all products from the cart
    def remove_all_products_from_cart(self):
        cart_products = self.wait_for_elements(self.CART_PRODUCTS_LOCATOR)
        expected_product_names = TestData.product_names

        for expected_product in expected_product_names:
            product_removed = False
            while not product_removed:
                for cart_product in cart_products:
                    try:
                        if expected_product in cart_product.text:
                            remove_button = cart_product.find_element(By.XPATH, self.REMOVE_BUTTON_LOCATOR)
                            remove_button.click()
                            product_removed = True
                    except StaleElementReferenceException:
                        cart_products = self.wait_for_elements(self.CART_PRODUCTS_LOCATOR)

        time.sleep(3)
        checkout_btn = self.wait_for_element(self.CHECKOUT_BUTTON_LOCATOR)
        checkout_btn.click()
