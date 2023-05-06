from faker import Faker
from factory import SubFactory
from factory.django import DjangoModelFactory
from ..models import Role, User, UserLocation, UserPersonalInfo
from common.utils.string_utils import generate_valid_login, generate_valid_password

fake = Faker(locale="ru_RU")


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role
        django_get_or_create = ("name",)

    name = fake.pystr()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    login = generate_valid_login()
    password = generate_valid_password()
    role = SubFactory(RoleFactory)


class UserPersonalInfoFactory(DjangoModelFactory):
    class Meta:
        model = UserPersonalInfo

    user = SubFactory(UserFactory)
    first_name = fake.first_name()
    second_name = fake.last_name()
    patronymic = fake.last_name()
    email = fake.email()
    gender = fake.simple_profile()["sex"]
    age = fake.random_number(digits=2)
    health_status = fake.text(max_nb_chars=10000)


class UserLocationFactory(DjangoModelFactory):
    class Meta:
        model = UserLocation

    user = SubFactory(User)
    country = fake.country()
    city = fake.city()
    address = fake.address()
