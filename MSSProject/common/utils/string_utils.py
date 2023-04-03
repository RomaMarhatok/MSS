import re
import exrex
import hashlib
from random import shuffle

from django.template.defaultfilters import slugify


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


def generate_slug_from_str(string: str):
    string = [i for i in string if re.match("^[a-zA-Z0-9_]*$", i)]
    shuffle(string)
    return slugify("".join(string))
