"""
filename: tests/allure_test.py
sources: https://github.com/allure-framework/allure-python/tree/master/allure-pytest/examples
"""
import pytest
import allure


@pytest.mark.allure_options
class TestAllureOptions():
    """Tbd"""

    @pytest.mark.inline_step
    def test_inline_step(self):
        """Tbd"""
        with allure.step("inline step"):
            pass

    @allure.step
    def passed_step(self):
        """Tbd"""

    @pytest.mark.reusable_step
    def test_reusable_step(self):
        """Tbd"""
        self.passed_step()

    @pytest.mark.nested_steps
    def test_nested_steps(self):
        """Tbd"""
        with allure.step("grand parent step"):
            with allure.step("parent step"):
                self.passed_step()

    @allure.step("class method as step")
    def class_method(self):
        """Tbd"""

    @pytest.mark.class_method_as_step
    def test_class_method_as_step(self):
        """Tbd"""
        self.class_method()
