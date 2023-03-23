import re


class TextValidator:
    @staticmethod
    def is_valid(value: str, regex=r"^[a-zA-Z\p{Cyrillic}]{1,}$") -> bool:
        return bool(re.match(regex, value))
