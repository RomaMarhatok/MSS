import dateutil.parser
from datetime import datetime


def parse_date_iso_format(string) -> str:
    parsed_date: datetime = dateutil.parser.isoparse(string)
    return (
        str(parsed_date.day)
        + "/"
        + str(parsed_date.month)
        + "/"
        + str(parsed_date.year)
    )
