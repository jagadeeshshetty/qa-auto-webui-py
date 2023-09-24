""" filename: tests/login_test.py """
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin():
    """Tbd"""
    @pytest.fixture
    def driver(self, request):
        """
        By default fixture methods in pytest are called around each test method.
        So we'll use this to setup and teardown our instance of Selenium.

        The driver method has two parameters, self and request .
        self is a required parameter for class methods, request is a parameter made available to fixtures.
        It enables access to loads of things during a test run.
        For now, the relevant piece is the ability to call request.addfinalizer .
        Actions passed to addfinalizer get executed after a test method completes. So we're calling
        driver_.quit() and passing it into the addfinalizer method.
        """
        # _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        # driver_ = webdriver.Firefox(executable_path=_geckodriver)
        driver_ = webdriver.Chrome()

        def quit():
            """ Tbd """
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self, driver):
        """ Tbd """
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)
        assert driver.find_element(By.CSS_SELECTOR, ".flash.success").is_displayed()
