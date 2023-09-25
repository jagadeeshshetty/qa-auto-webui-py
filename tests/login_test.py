""" filename: tests/login_test.py """
import time
import pytest
from selenium import webdriver
from pages import login_page


class TestLogin():
    """Tbd"""
    @pytest.fixture
    def login(self, request):
        """ tbd """
        driver_ = webdriver.Chrome()

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
