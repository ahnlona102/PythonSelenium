from enums.seat_type import SeatType
from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TicketPricePage(BasePage):
    def __init__(self):
        super().__init__()
        self.seat_type_locator = "//tr[td[text()='%s']]//a[text()='Book ticket']"
        self.price_of_seat_type = ("//table[@class='MyTable MedTable']//th[normalize-space()='Price ("
                                   "VND)']//following-sibling::td[count(//td[text()='%s']/preceding-sibling::td)+1]")
        self.ticket_price_tab_header = (By.XPATH, "//table[@class='MyTable MedTable']//tr["
                                                  "@class='TableSmallHeader']/th[contains(text(),'Ticket price from')]")
        self.section_locator = "//tr[td/li[text()='%s']]//a[contains(@href, 'TicketPricePage')]"

    def select_seat_type(self, user: User):
        seat_type = (By.XPATH, self.seat_type_locator % user.get_seat_type())
        self.scroll(seat_type)
        self.click(seat_type)

    def get_header_of_seat_price_table(self) -> bool:
        return self.get_text(self.ticket_price_tab_header)

    def get_price_of_seat_type(self, typee: SeatType) -> int:
        price_seat = (By.XPATH, self.price_of_seat_type % typee.value())
        price = self.get_text(price_seat)
        return int(price)

    def check_price_with_section(self, section):
        section_link = (By.XPATH, self.section_locator % section)
        self.click(section_link)

    def get_total_price_for_tickets(self, seat_type: SeatType, user: User):
        price_of_one_ticket = self.get_price_of_seat_type(seat_type)
        amount_ticket = int(user.get_amount_ticket())
        return price_of_one_ticket * amount_ticket
