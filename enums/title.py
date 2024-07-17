from enum import Enum


class Title(Enum):
    PASSWORD_CHANGE_FORM = "Password Change Form"

    def get_value(self) -> str:
        return self.value
