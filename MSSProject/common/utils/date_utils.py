import dateutil.parser
from datetime import datetime


def parse_date_iso_format(string) -> datetime:
    return dateutil.parser.isoparse(string)
