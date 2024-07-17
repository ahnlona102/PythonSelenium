from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.welcome_locator = (By.XPATH, "//div[@class='account']//strong")

    def get_welcome_message(self):
        return self.get_text(self.welcome_locator)
