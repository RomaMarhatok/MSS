from userApp.utils.date_utils import parse_date_iso_format


def test_parse():
    iso_date = "2022-12-27T13:46:06.422246Z"
    date = parse_date_iso_format(iso_date)
    assert date == "27/12/2022"
