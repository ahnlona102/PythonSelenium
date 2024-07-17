from enum import Enum


class SuccessBookedTicket(Enum):
    DEPART_STATION = 0
    ARRIVE_STATION = 1
    SEAT_TYPE = 2
    DEPART_DATE = 3
    AMOUNT_TICKET = 6

    def get_value(self) -> str:
        return self.value
