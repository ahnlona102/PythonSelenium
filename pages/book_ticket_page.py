from enums.book_ticket import BookTicket
from enums.railway_tab import RailwayTab
from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.date_utils import DateUtils


class BookTicketPage(BasePage):
    date_date = "//select[@name='Date']//option[text()='%s']"
    book_ticket_button = By.XPATH, "//legend[text()='Book ticket form']/following-sibling::input"
    select_option = "//select[@name='%s']"

    def select_depart_date(self, date: int):
        formatted_date = DateUtils.get_formatted_date(date)
        select_date = By.XPATH, self.date_date % formatted_date
        self.find(select_date).click()

    def select(self, option_name: BookTicket, value: str):
        option = By.XPATH, self.select_option % option_name.value
        self.scroll(option)
        self.click(option)
        try:
            int_value = int(value)
            if 1 <= int_value <= 10:
                self.select_by_value(option, value)
            else:
                self.select_by_visible_text(option, value)
        except ValueError:
            self.select_by_visible_text(option, value)

    def book_ticket_button(self):
        self.scroll(self.book_ticket_button)
        self.click(self.book_ticket_button)

    def book_multiple_tickets(self, number_of_tickets, start_date, user: User):
        options = [
            BookTicket.DEPARTSTATION,
            BookTicket.SEATTYPE,
            BookTicket.AMOUNTTICKET,
            BookTicket.ARRIVESTATION
        ]

        values = [user.get_depart(), user.get_seat_type(), user.get_amount_ticket(), user.get_arrive()]

        for i in range(number_of_tickets):
            self.click_tab(RailwayTab.BOOKTICKET)
            depart_date = start_date + i
            self.select_depart_date(depart_date)
            for j in range(len(options)):
                self.select(options[j], values[j])
            self.book_ticket_button()
