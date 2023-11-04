import allure
import pytest
from selenium import webdriver
import os
import time
import imageio
import threading
from contextlib import contextmanager


@allure.step('Add screenshot on test failure')
def allure_report_screenshot(driver, screenshot_name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG
    )


@allure.step('Add video on test failure')
def allure_report_video(video_path):
    allure.attach(
        open(video_path, 'rb').read(),
        name='video',
        attachment_type=allure.attachment_type.MP4
    )


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

# Function to start screen recording


def start_recording(driver, output_path):
    cmd = [
        "ffmpeg",
        "-y",
        "-f", "gdigrab",
        "-framerate", "30",
        "-offset_x", str(driver.get_window_position()["x"]),
        "-offset_y", str(driver.get_window_position()["y"]),
        "-video_size", str(driver.get_window_rect()["width"]) + "x" + str(driver.get_window_rect()["height"]),
        "-i", "desktop",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path
    ]
    os.system(" ".join(cmd))

# Function to stop screen recording


def stop_recording():
    os.system("taskkill /F /IM ffmpeg.exe")


@contextmanager
def screen_recording(driver, video_path):
    class RecordingThread(threading.Thread):
        def __init__(self, driver, video_path):
            super(RecordingThread, self).__init__()
            self.driver = driver
            self.video_path = video_path

        def run(self):
            try:
                start_recording(self.driver, self.video_path)
            except Exception as e:
                print(f"Failed to start recording: {e}")

    video_thread = RecordingThread(driver, video_path)
    video_thread.start()

    try:
        yield
    finally:
        stop_recording()
        video_thread.join()
