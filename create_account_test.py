import unittest

from enums.railway_tab import RailwayTab
from pages.base_page import BasePage
from pages.email_page import EmailPage
from pages.home_page import HomePage
from base_test import BaseTest
from pages.register_page import RegisterPage
from test_data.data_test import TestDataLoader
import threading
from models.User import User


class CreateAccountTest(BaseTest):
    base_page = BasePage()
    home_page = HomePage()
    email_page = EmailPage()
    register_page = RegisterPage()
    test_data_loader = TestDataLoader("data/test_data.json")

    def test_case7(self):
        test_data = self.test_data_loader.get_test_case('testCase7')
        user = User()
        user.set_email(test_data['email'])
        user.set_password(test_data['password'])
        user.set_confirm_password(test_data['confirm_password'])
        user.set_passport(test_data["passport"])
        error_message = test_data['error_message']
        print(f"Test 7 - {threading.current_thread().name}")
        self.base_page.navigate_to_url("railway.url")
        self.base_page.refresh_page()
        self.base_page.click_tab(RailwayTab.REGISTER)
        self.register_page.register_account(user)
        self.assertEqual(self.register_page.is_register_error_displayed(), error_message)

    def test_case8(self):
        test_data = self.test_data_loader.get_test_case('testCase8')
        user = User()
        user.set_email(test_data['username'] + test_data['domain'])
        error_message = test_data['error_message']
        password_error = test_data['password_field_err']
        passport_error = test_data['passport_field_err']
        print(f"Test 8 - {threading.current_thread().name}")
        self.base_page.navigate_to_url("railway.url")
        self.base_page.refresh_page()
        self.base_page.click_tab(RailwayTab.REGISTER)
        self.register_page.register_account(user)
        self.assertEqual(self.register_page.is_register_error_displayed(), error_message)
        self.assertTrue(self.register_page.is_field_error(password_error))
        self.assertTrue(self.register_page.is_field_error(passport_error))

    def test_case9(self):
        test_data = self.test_data_loader.get_test_case('testCase9')
        user = User()
        user.set_email(test_data['username'] + test_data['domain'])
        user.set_password(test_data['password'])
        user.set_confirm_password(test_data['confirm_password'])
        user.set_passport(test_data["passport"])
        title = test_data['title_thanks']
        success_message = test_data['success_message']
        self.base_page.navigate_to_url("mail.url")
        self.email_page.get_email(user)
        self.base_page.navigate_to_url("railway.url")
        self.base_page.click_tab(RailwayTab.REGISTER)
        self.register_page.register_account(user)
        self.register_page.is_title_display()




if __name__ == '__main__':
    unittest.main()
