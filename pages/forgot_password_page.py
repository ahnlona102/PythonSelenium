from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email_txtbox_locator = (By.XPATH, "//input[@id='email']")
        self.send_instruction_btn = (By.XPATH, "//input[@type='submit']")

    def submit_reset_password_form(self, user: User):
        self.enter_email(user)
        self.click_send_instruction_button()

    def enter_email(self, user: User):
        self.enter(self.email_txtbox_locator, user.email)

    def click_send_instruction_button(self):
        self.scroll(self.send_instruction_btn)
        self.click(self.send_instruction_btn)
