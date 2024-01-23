# checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME_FIELD_LOCATOR = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME_FIELD_LOCATOR = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE_FIELD_LOCATOR = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//input[@id='continue']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_shipping_info(self, first_name, last_name, zip_code):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)

        # Locate and wait for the first name input field
        first_name_field = wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD_LOCATOR))
        # Enter the provided first name into the field
        first_name_field.send_keys(first_name)

        # Locate and wait for the last name input field
        last_name_field = wait.until(EC.presence_of_element_located(self.LAST_NAME_FIELD_LOCATOR))
        # Enter the provided last name into the field
        last_name_field.send_keys(last_name)

        # Locate and wait for the zip code input field
        zip_code_field = wait.until(EC.presence_of_element_located(self.ZIP_CODE_FIELD_LOCATOR))
        # Enter the provided zip code into the field
        zip_code_field.send_keys(zip_code)

        # Locate and wait for the continue button
        continue_btn = wait.until(EC.presence_of_element_located(self.CONTINUE_BUTTON_LOCATOR))
        # Click the continue button to proceed to the next step
        continue_btn.click()
