import unittest

from base_test import BaseTest
from enums.book_ticket import BookTicket
from enums.railway_tab import RailwayTab
from models.User import User
from pages.base_page import BasePage
from pages.book_ticket_page import BookTicketPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_ticket_page import MyTicketPage
from test_data.data_test import TestDataLoader


class CancelTest(BaseTest):
    base_page = BasePage()
    home_page = HomePage()
    login_page = LoginPage()
    book_ticket_page = BookTicketPage()
    my_ticket_page = MyTicketPage()
    test_data_loader = TestDataLoader("data/test_data.json")

    def test_case6(self):
        try:
            test_data = self.test_data_loader.get_test_case('testCase16')
            user = User(test_data['email'], test_data['password'], test_data['depart'], test_data['amount_ticket'],
                        test_data['seat_type'], test_data['depart_date'], test_data['arrive'])

            self.base_page.navigate_to_railway()
            self.home_page.click_tab(RailwayTab.LOGIN)
            self.login_page.login(user)
            self.login_page.click_tab(RailwayTab.BOOKTICKET)
            self.book_ticket_page.select(BookTicket.DEPARTSTATION, user.get_depart())
            self.book_ticket_page.select(BookTicket.AMOUNTTICKET, user.get_amount_ticket())
            self.book_ticket_page.select(BookTicket.SEATTYPE, user.get_seat_type())
            self.book_ticket_page.select(BookTicket.DEPARTDATE, user.get_depart_date())
            self.book_ticket_page.select(BookTicket.ARRIVESTATION, user.get_arrive())
            self.book_ticket_page.book_ticket_button()
            self.book_ticket_success_page.click_tab(RailwayTab.MYTICKET)
            self.my_ticket_page.cancel_ticket(user)
            self.my_ticket_page.accept_cancel_ticket()
            self.assertTrue(self.my_ticket_page.is_cancelled_ticket_displayed(user))
        except AssertionError:
            self.capture_screenshot("login_testcase6_failure")
            raise


if __name__ == '__main__':
    unittest.main()
