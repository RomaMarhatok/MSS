import exrex
import hashlib


def generate_random_string_by_regex(re) -> str:
    return exrex.getone(re)


def generate_valid_password() -> str:
    regex = r"^[a-zA-Z0-9]{8,15}$"
    return generate_random_string_by_regex(regex)


def generate_valid_login() -> str:
    regex = r"^[a-zA-Z0-9_-]{3,16}$"
    return generate_random_string_by_regex(regex)


def generate_hash_from_string(hashing_string: str) -> str:
    return hashlib.sha256(hashing_string.encode("utf-8")).hexdigest()
