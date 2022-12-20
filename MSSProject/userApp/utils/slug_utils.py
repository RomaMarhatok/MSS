import re
from django.template.defaultfilters import slugify
from random import shuffle


def generate_slug_from_str(string: str):
    string = [i for i in string if re.match("^[a-zA-Z0-9_]*$", i)]
    shuffle(string)
    return slugify("".join(string))
