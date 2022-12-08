import re


class PasswordValidator:
    @staticmethod
    def is_valid(value: str, regex=r"^[a-zA-Z0-9!@#$%^&*]{8,15}$") -> bool:
        return bool(re.match(regex, value))
