from enum import Enum


class MyTicket(Enum):
    FILTER_DEPARTSTATION = "FilterDpStation"
    FILTER_ARRIVALSTATION = "FilterArStation"
    FILTER_DEPARTDATE = "FilterDpDate"

    def get_value(self):
        return self.value
