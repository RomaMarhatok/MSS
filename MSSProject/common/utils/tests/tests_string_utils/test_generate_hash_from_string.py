from common.utils.string_utils import generate_hash_from_string


def test_hash_generator():
    s1 = "622011_XutF2N1_hjo6aqa"
    s2 = "string2"
    print(generate_hash_from_string(s1))
    print(generate_hash_from_string(s1))
    print(generate_hash_from_string(s1))

    assert generate_hash_from_string(s1) == generate_hash_from_string(s1)
    assert generate_hash_from_string(s2) == generate_hash_from_string(s2)
    assert generate_hash_from_string(s1) != generate_hash_from_string(s2)
