from enum import Enum


class ResetPassword(Enum):
    NEWPASS = "password"
    IDNEWPASS = "newPassword"
    CONFIRMNEWPASS = "password"
    IDCONFIRMNEWPASS = "confirmPassword"
    RESETBUTTON = "Reset password"

    def get_value(self) -> str:
        return self.value
