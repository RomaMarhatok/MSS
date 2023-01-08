import dateutil.parser
from datetime import datetime


def format_date(str_date):
    return str_date if len(str_date) == 2 else "0" + str(str_date)


def parse_date_iso_format(string) -> str:
    parsed_date: datetime = dateutil.parser.isoparse(string)

    return (
        str(parsed_date.day)
        + "/"
        + str(parsed_date.month)
        + "/"
        + str(parsed_date.year)
        + " "
        + format_date(str(parsed_date.hour))
        + ":"
        + format_date(str(parsed_date.minute))
    )
