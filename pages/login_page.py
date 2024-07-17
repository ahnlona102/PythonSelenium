from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from models.User import User


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email_textbox_locator = (By.ID, "username")
        self.password_textbox_locator = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@value='login']")
        self.login_error = (By.XPATH, "//p[contains(@class,'message error')]")

    def enter_mail(self, user: User):
        self.clear_field(self.email_textbox_locator)
        self.enter(self.email_textbox_locator, user.get_email())

    def enter_password(self, user: User):
        self.enter(self.password_textbox_locator, user.get_password())

    def click_login(self):
        self.scroll(self.login_button)
        self.click(self.login_button)

    def login(self, user: User):
        self.enter_mail(user)
        self.enter_password(user)
        self.click_login()

    def login_many_times(self, user: User, number: int):
        for _ in range(number - 1):
            self.login(user)

    def is_login_error_message_displayed(self):
        actual_message = self.get_text(self.login_error)
        return actual_message
