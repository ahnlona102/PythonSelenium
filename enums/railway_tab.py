from enum import Enum


class RailwayTab(Enum):
    HOME = "Home"
    FAQ = "FAQ"
    CONTACT = "Contact"
    TIMETABLE = "Timetable"
    TICKETPRICE = "Ticket price"
    REGISTER = "Register"
    LOGIN = "Login"
    MYTICKET = "My ticket"
    BOOKTICKET = "Book ticket"
    CHANGEPASSWORD = "Change password"
    LOGOUT = "Log out"

    def get_value(self) -> str:
        return self.value
