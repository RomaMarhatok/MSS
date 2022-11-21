from factory.django import DjangoModelFactory
from faker import Faker

from ...models import Roles

fake = Faker()


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Roles

    name = fake.pystr()
