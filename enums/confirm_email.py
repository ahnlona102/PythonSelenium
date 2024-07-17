from enum import Enum


class ConfirmEmail(Enum):
    CONFIRM = "Please confirm"
    RESET = "Please reset"

    def get_value(self) -> str:
        return self.value
