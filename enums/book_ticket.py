from enum import Enum


class BookTicket(Enum):
    DEPARTDATE = "Date"
    DEPARTSTATION = "DepartStation"
    ARRIVESTATION = "ArriveStation"
    SEATTYPE = "SeatType"
    AMOUNTTICKET = "TicketAmount"

    def get_value(self) -> str:
        return self.value
