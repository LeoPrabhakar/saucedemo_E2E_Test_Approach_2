import pytest
from selenium import webdriver
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    ChromeDriverManager().install()
    driver = webdriver.Chrome(webdriver.ChromeOptions())
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()
