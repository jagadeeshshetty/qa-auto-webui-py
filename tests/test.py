import pytest
from conftest import allure_report_screenshot, allure_report_video, screen_recording
import os
import time
import allure
import imageio
import threading
from selenium import webdriver


@pytest.mark.parametrize("search_query", ["Selenium", "Python", "Allure"])
def test_search_google(driver, search_query):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.find_element_by_name("q").send_keys(search_query)
    driver.find_element_by_name("btnK").click()
    assert search_query in driver.title


@pytest.mark.search_google_record
def test_search_google_record(driver):
    video_path = "video.mp4"

    with screen_recording(driver, video_path):
        driver.get("https://www.google.com")
        assert driver.title == "Google"
        driver.find_element_by_name("q").send_keys("Selenium")
        driver.find_element_by_name("btnK").click()
        assert "Selenium" in driver.title

    allure.attach.file(video_path, "Video Recording", attachment_type=allure.attachment_type.MP4)
