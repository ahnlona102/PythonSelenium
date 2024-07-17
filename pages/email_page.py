from selenium.webdriver.common.by import By

from enums.confirm_email import ConfirmEmail
from pages.base_page import BasePage
from models.User import User


class EmailPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username_textbox_locator = (By.XPATH, "//span[@id='inbox-id']")
        self.user_txtbox_locator = "//span[@id='inbox-id']//input[@type='text']"
        self.domain_select_locator = (By.ID, "gm-host-select")
        self.set_btn = (By.XPATH, "//span[@id='inbox-id']//button[1]")
        self.checkbox_locator = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.email_field_locator = (By.ID, "email-widget")
        self.confirm_link_locator = (By.XPATH, "//a[contains(@href, 'saferailway')]")
        self.confirm_mess = "//td[contains(text(), '%s')]"
        self.mail_content = (By.XPATH, "//div[@class='email_body']")

    def get_email(self, user: User) -> str:
        self.get_wait(10)
        self.click_if_clickable(self.username_textbox_locator)
        self.enter_username(user)
        self.select_domain(user)
        self.click(self.set_btn)
        self.click(self.checkbox_locator)
        get_email = self.get_text(self.email_field_locator)
        print("Get Email:", get_email)
        return get_email

    def enter_username(self, user: User):
        xpath = self.user_txtbox_locator
        username_input = (By.XPATH, xpath)
        self.enter(username_input, user.get_username())

    def select_domain(self, user: User):
        self.select_by_value(self.domain_select_locator, user.get_domain())

    def click_set_btn(self):
        self.click(self.set_btn)
        self.get_wait(20)

    def set_mail(self, user: User):
        self.get_wait(10)
        self.click_if_clickable(self.username_textbox_locator)
        self.enter_username(user)
        self.select_domain(user)
        self.click_set_btn()

    def check_confirm_mess(self, text: ConfirmEmail):
        self.get_wait(20)
        mess = (By.XPATH, self.confirm_mess_locator % text.value)
        self.click(mess)

    def click_confirm_link(self):
        self.get_wait(50)
        self.click_if_clickable(self.confirm_link_locator)

    def confirm_email(self, text: ConfirmEmail):
        self.get_wait(30)
        self.check_confirm_mess(text)
        self.click_confirm_link()

    def get_reset_password_token(self) -> str:
        mail_content = self.get_text(self.mail_content)
        parts = mail_content.split("The token is: ")
        if len(parts) > 1:
            token_part = parts[1].strip()
            token_parts = token_part.split()
            return token_parts[0]
        return ""
