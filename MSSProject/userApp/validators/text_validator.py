import re


class TextValidator:
    @staticmethod
    def is_valid(value: str, regex=r"^[a-zA-Z]{1,}$") -> bool:
        return bool(re.match(regex, value))
