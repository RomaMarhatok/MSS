import dateutil.parser
from datetime import datetime


def format_date(str_date):
    return str_date if len(str_date) == 2 else "0" + str(str_date)


def parse_date_iso_format(string) -> datetime:
    return dateutil.parser.isoparse(string)
