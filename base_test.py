import unittest
import os
import argparse
from PIL import ImageGrab

from utils.config_loader import ConfigLoader
from utils.driver_manager import DriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        parser = argparse.ArgumentParser(description='Run tests with specified WebDriver type and browser.')
        parser.add_argument('--type', required=True, choices=['local', 'remote'])
        parser.add_argument('--browser', required=True, choices=['chrome', 'firefox', 'edge'])
        # args, _ = parser.parse_known_args()
        args = parser.parse_args()
        config_loader = ConfigLoader()
        config_loader.load_properties()
        type_arg = args.type.lower()
        browser_arg = args.browser.lower()

        self.driver_manager = DriverManager()

        if type_arg == "remote":
            self.driver_manager.init_remote_webdiver(browser_arg)
            self.driver_manager.getDriver().maximize_window()
        else:
            self.driver_manager.init_local_webdiver(browser_arg)
            self.driver_manager.getDriver().maximize_window()

    def tearDown(self):
        self.driver_manager.quitDriver()

    def capture_screenshot(self, filename):
        screenshot = ImageGrab.grab()
        screenshot_path = f'screenshots/{filename}.png'
        screenshot.save(screenshot_path)
        return screenshot_path
