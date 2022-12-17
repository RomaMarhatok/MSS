from userApp.utils.list_utils import is_containe


def test_with_valid_data():
    mass1 = [1, 2]
    mass2 = [1, 2, 3, 4]
    assert is_containe(mass1, mass2)
    mass1 = ["login", "password"]
    mass2 = ["login", "password"]
    assert is_containe(mass1, mass2)


def test_with_invalid_data():
    mass1 = [1, 2]
    mass2 = [3, 4]
    assert not is_containe(mass1, mass2)
    mass1 = ["login", "password"]
    mass2 = ["login"]
    assert not is_containe(mass1, mass2)
