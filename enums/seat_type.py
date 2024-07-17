from enum import Enum


class SeatType(Enum):
    SOFTSEAT = "SS"
    HARDSEAT = "HS"
    SOFTSEATWITHAIRCONDITIONER = "SSC"
    HARDBED = "HB"
    SOFTBED = "SB"
    SOFTBEDWITHAIRCONDITIONER = "SBC"

    def get_value(self) -> str:
        return self.value
