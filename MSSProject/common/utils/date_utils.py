import dateutil.parser
from datetime import datetime


def parse_date_to_dict(string, short: bool = False) -> dict:
    dt = dateutil.parser.isoparse(string)
    mounth_names = [
        "Января",
        "Февраля",
        "Марта",
        "Апреля",
        "Мая",
        "Июня",
        "Июля",
        "Августа",
        "Сентября",
        "Октября",
        "Ноября",
        "Декабря",
    ]
    short_names = [
        "Янв",
        "Февр",
        "Март",
        "Апр",
        "Мая",
        "Июня",
        "Июля",
        "Авг",
        "Сент",
        "Окт",
        "Нояб",
        "Дек",
    ]
    return {
        "mounth": mounth_names[dt.month - 1]
        if not short
        else short_names[dt.month - 1],
        "day": dt.day if len(str(dt.day)) == 2 else "0" + str(dt.day),
        "hours": dt.hour if len(str(dt.hour)) == 2 else "0" + str(dt.hour),
        "minutes": dt.minute if len(str(dt.minute)) == 2 else "0" + str(dt.minute),
        "year": dt.year,
    }
