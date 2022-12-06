import re


class PasswordValidator:
    @staticmethod
    def is_valid(password: str, regex=r"^[a-zA-Z0-9!@#$%^&*]{8,15}$") -> bool:
        return bool(re.match(regex, password))
