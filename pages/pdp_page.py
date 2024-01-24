# pdp_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


# PDPPage class inherits from BasePage
class PDPPage(BasePage):
    # locators
    ADD_TO_CART_BUTTON_LOCATOR = '//button[@class="btn btn_primary btn_small btn_inventory"]'
    CART_BUTTON_LOCATOR = "//a[@class='shopping_cart_link']"

    def __init__(self, driver):
        super().__init__(driver)

    # # Method to add a product to the cart and view the cart
    # def add_to_cart(self):
    #     # Set up a WebDriverWait instance with a timeout of 10 seconds
    #     wait = WebDriverWait(self.driver, 10)
    #     # Locate and wait for the "Add to Cart" button on the product detail page
    #     add_to_cart_btn = wait.until(EC.presence_of_element_located(
    #         (By.XPATH, self.ADD_TO_CART_BUTTON_LOCATOR)))
    #     # Click the "Add to Cart" button to add the product to the cart
    #     add_to_cart_btn.click()
    #     # Introduce a delay (using time.sleep) to ensure the cart icon updates properly
    #     time.sleep(2)
    #     # Locate and wait for the shopping cart icon to view the cart
    #     cart_btn_click = wait.until(EC.presence_of_element_located((By.XPATH, self.CART_BUTTON_LOCATOR)))
    #     # Click the shopping cart icon to view the cart
    #     cart_btn_click.click()

    # Method to add a product to the cart and view the cart
    def add_to_cart(self):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for the shopping cart icon on the page
        cart_btn_click = wait.until(EC.presence_of_element_located((By.XPATH, self.CART_BUTTON_LOCATOR)))
        # Click the shopping cart icon to view the cart
        cart_btn_click.click()

