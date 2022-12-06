from userApp.utils.string_utls import generate_random_string_by_regex


def test_generate_random_string_by_regex():
    regex = r"^[a-zA-Z0-9!@#$%^&*]{8,15}$"
    result_list_without_dublicates = {
        generate_random_string_by_regex(regex) for _ in range(100)
    }

    assert len(result_list_without_dublicates) == 100
