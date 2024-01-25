# test_script.py
import pytest
from Saucedemo_new_Approach2_E2E_test.pages.login_page import LoginPage
from Saucedemo_new_Approach2_E2E_test.pages.logout_page import Logout
from selenium.webdriver.common.by import By
from ddt import ddt, data, file_data, unpack


# Using pytest.mark.usefixtures to set up the test environment
@pytest.mark.usefixtures("setup")
# @ddt
class TestEndToEnd:
    # Approach1
    @pytest.mark.parametrize(("username_param", "password_param"), [
        # ("standard_user", "secret_sauce"),
        ("standard_user123", "secret_sauce123"),
        ("standard_user123", "secret_sauce"),
        ("standard_user", "secret_sauce123"),
        ("", "")
    ])
    # Approach2
    # # @data(("standard_user", "secret_sauce"),
    #       ("standard_user123", "secret_sauce123"),
    #       ("", ""))
    # @file_data("../testData/login_input.json")
    def test_end_to_end_flow(self, username_param, password_param):
        # Instantiate LoginPage class
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(username_param, password_param)
        # actual_title_element = self.find_element(By.XPATH, "//span[@class='title']")
        # actual_title = actual_title_element.text
        actual_error_msg_element = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        actual_error_msg = actual_error_msg_element.text
        # expected_title = ["Products"]
        expected_error_msg = [
            "Epic sadface: Username and password do not match any user in this service",
            "Epic sadface: Username is required"
        ]
        # Check if the actual error message is one of the expected messages
        assert actual_error_msg in expected_error_msg, f"Unexpected error message: {actual_error_msg}"
        # if actual_title in expected_title:
        #     home_page = Logout(self.driver)
        #     home_page.logout()

