import concurrent.futures
import threading
import unittest

from XTestRunner import HTMLTestRunner

from base_test import BaseTest
from enums.railway_tab import RailwayTab
from models.User import User
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.data_test import TestDataLoader


class LoginTest(BaseTest):
    base_page = BasePage()
    home_page = HomePage()
    login_page = LoginPage()
    test_data_loader = TestDataLoader("data/test_data.json")

    def test_case1(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase1')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            expected_message = test_data['expected_message']
            print(f"Test 1 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.assertEqual(expected_message, self.home_page.get_welcome_message(),
                             f"Expected '{'Welcome' + user.get_email()}'")
        except AssertionError:
            self.capture_screenshot("login_testcase1_failure")
            raise

    def test_case2(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase2')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            error_message = test_data['error_message']
            print(f"Test 2 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.enter_password(user)
            self.login_page.click_login()
            self.assertEqual(error_message, self.login_page.is_login_error_message_displayed())
        except AssertionError:
            self.capture_screenshot("login_testcase2_failure")
            raise

    def test_case3(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase3')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            error_message = test_data['error_message']
            print(f"Test 3 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.assertEqual(error_message, self.login_page.is_login_error_message_displayed())
        except AssertionError:
            self.capture_screenshot("login_testcase3_failure")
            raise

    def test_case4(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase4')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            error_message = test_data['error_message']
            attemp_error_message = test_data['attemp_error_message']
            print(f"Test 4 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.assertEqual(error_message, self.login_page.is_login_error_message_displayed())
            self.login_page.login_many_times(user, 5)
            self.assertEqual(self.login_page.is_login_error_message_displayed(), attemp_error_message)
        except AssertionError:
            self.capture_screenshot("login_testcase4_failure")
            raise

    def test_case5(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase5')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            error_message = test_data['error_message']
            print(f"Test 5 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.assertEqual(error_message, self.login_page.is_login_error_message_displayed())
        except AssertionError:
            self.capture_screenshot("login_testcase5_failure")
            raise


if __name__ == '__main__':
    unittest.main()
