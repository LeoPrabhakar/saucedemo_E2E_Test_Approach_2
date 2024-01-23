# confirmation_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


# ConfirmationPage class inherits from BasePage
class ConfirmationPage(BasePage):
    # Locator
    FINISH_BUTTON_LOCATOR = "//button[@id='finish']"

    def __init__(self, driver):
        super().__init__(driver)

    # Method to complete the checkout process
    def complete_checkout(self):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for the "Finish" button
        finish_btn = wait.until(EC.presence_of_element_located((By.XPATH, self.FINISH_BUTTON_LOCATOR)))
        # Click the "Finish" button to complete the checkout process
        finish_btn.click()


