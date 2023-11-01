""" filename: tests/login_test.py """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

from pages import login_page


@pytest.mark.the_internet
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

    @pytest.mark.valid_login
    def test_valid_credentials(self, login):
        """ Tbd """
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    @pytest.mark.invalid_login
    def test_invalid_credentials(self, login):
        """ Tbd """
        login.with_("tomsmith", "bad password")
        assert login.failure_message_present()
