from random import shuffle
import re


def generate_slug_from_str(string: str):
    string = [i for i in string if re.match("^[a-zA-Z0-9_]*$", i)]
    shuffle(string)
    return "".join(string)
