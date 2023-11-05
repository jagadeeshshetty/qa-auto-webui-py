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

    @allure.link("http://qameta.io")
    def test_link(self):
        pass

    @allure.issue("https://github.com/allure-framework/allure-python/issues/24")
    def test_issue_link(self):
        pass

    @allure.testcase("issues/24#issuecomment-277330977")
    def test_testcase_link(self):
        pass

    @allure.link("http://qameta.io", name="QAMETA", link_type="homepage")
    def test_custom_link(self):
        pass

    def test_attach_body_with_default_kwargs(self):
        allure.attach("Some content in plain text")

    def test_attach_body(self):
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
        <tag>
            <inside>...</inside>
        </tag>
        """
        allure.attach(xml_content, name='some attachment name', attachment_type=allure.attachment_type.XML)
        allure.attach("Some content in plain text")

    def test_attach_file(self):
        allure.attach.file(__file__)  # this file path
