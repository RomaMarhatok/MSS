import exrex


def generate_random_string_by_regex(re) -> str:
    return exrex.getone(re)


def generate_valid_password() -> str:
    regex = r"^[a-zA-Z0-9!@#$%^&*]{8,15}$"
    return generate_random_string_by_regex(regex)


def generate_valid_login() -> str:
    regex = r"^[a-zA-Z0-9_-]{3,16}$"
    return generate_random_string_by_regex(regex)
