# login_page.py
from Saucedemo_new_Approach2_E2E_test.base.base_file import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# LoginPage class inherits from BasePage
class LoginPage(BasePage):
    # locators
    USER_NAME_LOCATOR = "//input[@id='user-name']"
    PASSWORD_LOCATOR = "//input[@id='password']"
    LOGIN_BUTTON_LOCATOR = "//input[@id='login-button']"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    # Method to open the login page
    def open(self):
        # Navigate to the specified URL
        self.driver.get(self.url)
        # Maximize the browser window for better visibility
        self.driver.maximize_window()

    # Method to perform login with provided username and password
    def login(self, username, password):
        # Set up a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, 10)
        # Locate and wait for the username input field
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, self.USER_NAME_LOCATOR)))
        # Enter the provided username into the field
        username_field.send_keys(username)
        # Locate and wait for the password input field
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, self.PASSWORD_LOCATOR)))
        # Enter the provided password into the field
        password_field.send_keys(password)
        # Locate and wait for the login button
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, self.LOGIN_BUTTON_LOCATOR)))
        # Click the login button to submit the login credentials
        login_button.click()

