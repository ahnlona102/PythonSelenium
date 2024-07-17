from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from models.User import User


class RegisterPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email_textbox_locator = (By.NAME, "email")
        self.password_textbox_locator = (By.NAME, "password")
        self.confirm_pass_locator = (By.ID, "confirmPassword")
        self.passport_textbox_locator = (By.NAME, "pid")
        self.register_btn = (By.XPATH, "//input[@title='Register']")
        self.register_err_locator = (By.XPATH, "//p[@class='message error']")
        self.invalid_error_locator = "//label[contains(text(),'%s')]"
        self.message_locator = "//p[contains(text(),'%s')]"

    def register_account(self, user: User):
        self.enter(self.email_textbox_locator, user.get_email())
        self.enter(self.password_textbox_locator, user.get_password())
        self.enter(self.confirm_pass_locator, user.get_confirm_password())
        self.enter(self.passport_textbox_locator, user.get_passport())
        self.click_register_button()

    def click_register_button(self):
        self.scroll(self.register_btn)
        self.click(self.register_btn)

    def is_register_error_displayed(self):
        actual = self.get_text(self.register_err_locator)
        return actual

    def is_field_error(self, message: str):
        field_error = (By.XPATH, self.invalid_error_locator % message)
        return field_error

    def is_message_displayed(self, message: str):
        message_locate = (By.XPATH, self.message_locator % message)
        return self.is_displayed(message_locate)
