from enums.success_booked_ticket import SuccessBookedTicket
from models import User
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BookTicketSuccessPage(BasePage):
    message = By.XPATH, "//h1[@align='center']"
    table_info = By.XPATH, "//table[@class='MyTable WideTable']"

    def is_success_message_displayed(self):
        success_message = self.get_text(self.message)
        return success_message

    def is_information_displayed(self, user: User) -> bool:
        table = self.find(self.table_info)
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 7:
                actual_depart_station = cells[SuccessBookedTicket.DEPART_STATION].text
                actual_arrive_station = cells[SuccessBookedTicket.ARRIVE_STATION].text
                actual_seat_type = cells[SuccessBookedTicket.SEAT_TYPE].text
                actual_depart_date = cells[SuccessBookedTicket.DEPART_DATE].text
                actual_amount = cells[SuccessBookedTicket.AMOUNT_TICKET].text
                return (actual_depart_station == user.depart and
                        actual_arrive_station == user.arrive and
                        actual_seat_type == user.seat_type and
                        actual_depart_date == user.depart_date and
                        actual_amount == str(user.amount_ticket))
        return False
