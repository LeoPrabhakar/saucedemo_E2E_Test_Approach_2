# plp_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


# PLPPage class inherits from BasePage
class PLPPage(BasePage):
    # locators
    INVENTORY_ITEM_LOCATOR = "//div[@class='inventory_list']//div[@class='inventory_item']"
    ADD_TO_CART_BUTTON_LOCATOR = './/button[@class="btn btn_primary btn_small btn_inventory "]'

    def __init__(self, driver):
        super().__init__(driver)

    # # Method to select single product from the Product List Page (PLP)
    # def select_product(self, product_name):
    #     # Set up a WebDriverWait instance with a timeout of 10 seconds
    #     wait = WebDriverWait(self.driver, 10)
    #
    #     # Locate and wait for all product elements on the page
    #     product_elements = wait.until(EC.presence_of_all_elements_located(
    #                     (By.XPATH, self.INVENTORY_ITEM_LOCATOR)))
    #
    #     # Iterate through each product element to find the desired product by name
    #     for product_element in product_elements:
    #         # Check if the desired product name is contained in the text of the current product element
    #         if product_name in product_element.text:
    #             # Click on the product element to select the product
    #             product_element.click()
    #             # Exit the loop after selecting the product
    #             break

# ---------------------------------------------------------------------------------------------------------

    # Method to select multiple products by name and add them to the cart
    def select_product(self, product_names):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for all product elements on the page
        product_elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, self.INVENTORY_ITEM_LOCATOR)))
        # Iterate through each provided product name
        for product_name in product_names:
            # Iterate through each product element on the page
            for product_element in product_elements:
                # Check if the desired product name is contained in the text of the current product element
                if product_name in product_element.text:
                    # Find the "Add to Cart" button within the product element using the XPath
                    add_to_cart_btn = product_element.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_LOCATOR)
                    # Click on the "Add to Cart" button to add the product to the cart
                    add_to_cart_btn.click()
                    # Introduce a delay (using time.sleep) to ensure proper processing
                    time.sleep(2)
                    # Exit the loop after clicking once for each product
                    break


