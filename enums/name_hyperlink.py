from enum import Enum


class NameHyperlink(Enum):
    FORGOTPASSWORD = "Forgot Password page"
    REGISTRATION = "registration page"

    def get_value(self) -> str:
        return self.value
