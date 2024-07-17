from enums.my_ticket import MyTicket
from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MyTicketPage(BasePage):
    def __init__(self):
        super().__init__()
        self.cancel_ticket_btn = ("//table[@class='MyTable']//tr[td[text()='%s' and following-sibling::td[text()='%s'"
                                  " and following-sibling::td[text()='%s' and following-sibling::td[text()='%s' "
                                  "and following-sibling::td[text()='%s']]]]]]//input[contains(@onclick, 'Delete')]")

        self.ticket_infor_row_locator = (
            "//table[@class='MyTable']//tr[td[text()='%s' and following-sibling::td[text()='%s'"
            " and following-sibling::td[text()='%s' and following-sibling::td[text()='%s' "
            "and following-sibling::td[text()='%s']]]]]]")

        self.table_filter_locator = "//table[@letxpath='letxpathtable']//td//select[@name='%s']"
        self.depart_date_filter_locator = (By.XPATH, "//input[@title='Empty = Ignore']")
        self.filter_btn_locator = (By.XPATH, "//input[@value='Apply filter']")

    def cancel_ticket(self, user: User):
        amount = str(user.amount_ticket)
        cancel_btn = (By.XPATH, self.cancel_ticket_btn % (
            user.depart, user.arrive, user.seat_type, user.depart_date, amount))
        self.scroll(cancel_btn)
        self.click(cancel_btn)

    def accept_cancel_ticket(self):
        self.accept_alert()

    def is_cancelled_ticket_displayed(self, user: User) -> bool:
        amount = str(user.amount_ticket)
        rows = (By.XPATH, self.ticket_infor_row_locator % (
            user.depart, user.arrive, user.seat_type, user.depart_date, amount))
        return self.is_disappear(rows)

    def select_field_filter(self, field: MyTicket, text):
        filter_locator = (By.XPATH, self.table_filter_locator % field.value)
        self.select_by_visible_text(filter_locator, text)

    def input_depart_date_filter(self, date):
        self.enter(self.depart_date_filter_locator, date)

    def click_filter_button(self):
        self.click(self.filter_btn_locator)

    def is_manage_table_shows_correct_ticket(self, user):
        amount = str(user.amount_ticket)
        rows_locator = (
        By.XPATH, self.ticket_info_row_locator % (user.get_depart(), user.get_arrive(), user.get_seat_type(), user.get_depart_date(), amount))
        return self.is_displayed(rows_locator)
