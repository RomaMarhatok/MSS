from enum import Enum


class EmailHost(Enum):
    GMAIL_HOST = 'smtp.gmail.com'
    MAIL_HOST = 'smtp.mail.ru'
    YANDEX_HOST = 'smtp.yandex.ru'
