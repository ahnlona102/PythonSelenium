import unittest
from enums.railway_tab import RailwayTab
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from base_test import BaseTest
from test_data.data_test import TestDataLoader
import threading
from models.User import User
from XTestRunner import HTMLTestRunner


class LogoutTest(BaseTest):
    base_page = BasePage()
    home_page = HomePage()
    login_page = LoginPage()
    test_data_loader = TestDataLoader("data/test_data.json")

    def test_case6(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase1')
            user = User()
            user.set_email(test_data['email'])
            user.set_password(test_data['password'])
            print(f"Test 6 - {threading.current_thread().name}")
            self.base_page.navigate_to_url("railway.url")
            self.base_page.refresh_page()
            self.base_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.base_page.click_tab(RailwayTab.FAQ)
            self.base_page.click_tab(RailwayTab.LOGOUT)
            self.assertTrue(self.base_page.is_tab_displayed(RailwayTab.HOME))
            self.assertTrue(self.base_page.does_tab_exist(RailwayTab.LOGOUT))
        except AssertionError:
            self.capture_screenshot("login_testcase6_failure")
            raise


if __name__ == '__main__':
    unittest.main()
# if __name__ == '__main__':
#     argv = ['']
#     suit = unittest.TestLoader()
#     suite = suit.loadTestsFromTestCase(LogoutTest)
#
#     report_file = 'reports/result.html'
#
#     with open(report_file, 'wb') as fp:
#         runner = HTMLTestRunner(
#             stream=fp,
#             title='Test Report',
#             description='Test Description',
#             language='en',
#         )
#         runner.run(suite)
