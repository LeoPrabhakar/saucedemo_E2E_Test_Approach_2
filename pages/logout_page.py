# home_page.py
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage


# Logout class inherits from BasePage
class Logout(BasePage):
    # locators
    BURGER_MENU_BUTTON_LOCATOR = "//button[@id='react-burger-menu-btn']"
    LOGOUT_BUTTON_LOCATOR = "//a[@id='logout_sidebar_link']"

    def __init__(self, driver):
        super().__init__(driver)

    # Method to perform logout
    def logout(self):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for the menu button
        menu_btn = wait.until(EC.presence_of_element_located((By.XPATH, self.BURGER_MENU_BUTTON_LOCATOR)))
        # Click the menu button to open the navigation menu
        menu_btn.click()
        # Introduce a delay (using time.sleep) to ensure proper rendering of the menu options
        time.sleep(2)
        # Locate and wait for the logout button within the menu
        logout_btn = wait.until(EC.presence_of_element_located((By.XPATH, self.LOGOUT_BUTTON_LOCATOR)))
        # Click the logout button to log out from the application
        logout_btn.click()

