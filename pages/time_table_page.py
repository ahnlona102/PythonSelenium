from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TimeTablePage(BasePage):
    def __init__(self):
        super().__init__()
        self.check_price_page_locator = ("//tr[td[text()='%s' and following-sibling::td[text()='%s']]]//a[contains("
                                         "@href, 'TicketPricePage')]")
        self.book_ticket_page_locator = ("//tr[td[text()='%s' and following-sibling::td[text()='%s']]]//a[contains("
                                         "@href, 'BookTicketPage')]")

    def check_price(self, user: User):
        check = (By.XPATH, self.check_price_page_locator % (user.get_depart(), user.get_arrive()))
        self.click(check)

    def book_ticket(self, user: User):
        book = (By.XPATH, self.book_ticket_page_locator % (user.get_depart(), user.get_arrive()))
        self.click(book)
