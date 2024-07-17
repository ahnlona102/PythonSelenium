from enums.reset_password import ResetPassword
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ResetPasswordPage(BasePage):
    def __init__(self):
        super().__init__()
        self.field_locator = "//input[@type='%s' and @id='%s']"
        self.form_name_locator = "//legend[contains(text(),'%s')]"
        self.pass_token_locator = (By.XPATH, "//input[@id='resetToken']")
        self.message_above_form = (By.XPATH, "//p[contains(@class,'message')]")
        self.message_next_confirm_password = (By.XPATH, "//label[@for='confirmPassword' and @class='validation-error']")

    def enter_field(self, field_name: ResetPassword, id_name: ResetPassword, value):
        field_locator = (By.XPATH, self.field_locator % (field_name.value, id_name.value))
        self.enter(self.find(field_locator), value)

    def click_button(self, button_name: ResetPassword):
        button_locator = (By.XPATH, self.field_locator % button_name.value)
        self.scroll(self.find(button_locator))
        self.click(self.find(button_locator))

    def is_title_form_displayed(self, name):
        title_locator = (By.XPATH, self.form_name_locator % name)
        return self.is_displayed(self.find(title_locator))

    def get_reset_token(self):
        return self.find(self.pass_token_locator).get_attribute("value")

    def get_message_above_form(self):
        return self.get_text(self.find(self.message_above_form))

    def get_message_next_confirm_password(self):
        return self.get_text(self.find(self.message_next_confirm_password))
