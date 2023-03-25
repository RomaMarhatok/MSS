import regex


class TextValidator:
    @staticmethod
    def is_valid(value: str, re=r"^[a-zA-Z\p{Cyrillic}]{1,}$") -> bool:
        return bool(regex.match(re, value))
