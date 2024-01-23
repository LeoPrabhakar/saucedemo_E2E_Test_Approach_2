# completion_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


class CompletionPage(BasePage):
    # Locator
    BACK_TO_PRODUCTS_BUTTON_LOCATOR = (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        super().__init__(driver)

    def back_to_home(self):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for the "Back to Products" button
        back_home_btn = wait.until(EC.presence_of_element_located(self.BACK_TO_PRODUCTS_BUTTON_LOCATOR))
        # Click the "Back to Products" button to go back to the home page
        back_home_btn.click()
