""" filename: tests/login_test.py """
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages import login_page


class TestLogin():
    """Tbd"""
    @pytest.fixture
    def login(self, request):
        """ tbd """
        chrome_options = Options()
        # Run Chrome in headless mode
        chrome_options.add_argument("--headless")
        driver_ = webdriver.Chrome(options=chrome_options)

        def quit():
            """ Tbd """
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid_credentials(self, login):
        """ Tbd """
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    def test_invalid_credentials(self, login):
        """ Tbd """
        login.with_("tomsmith", "bad password")
        assert login.failure_message_present()
