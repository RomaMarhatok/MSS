import re


class LoginValidator:
    @staticmethod
    def is_valid(value: str, regex=r"^[a-zA-Z0-9_-]{3,16}$") -> bool:
        return bool(re.match(regex, value))
