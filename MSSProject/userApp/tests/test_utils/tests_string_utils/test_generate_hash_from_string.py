from userApp.utils.string_utls import generate_hash_from_string


def test_hash_generator():
    s1 = "string1"
    s2 = "string2"
    assert generate_hash_from_string(s1) == generate_hash_from_string(s1)
    assert generate_hash_from_string(s2) == generate_hash_from_string(s2)
    assert generate_hash_from_string(s1) != generate_hash_from_string(s2)
