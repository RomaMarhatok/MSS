from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ...models import User
from ..factories.role_factory import RoleFactory

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("role",)

    username = fake.profile()["username"]
    login = fake.pystr()
    password = fake.password()
    role = SubFactory(RoleFactory)
