from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ...models import UserPersonalInfo
from ..factories.user_factory import UserFactory

fake = Faker()


class UserPersonalInfoFactory(DjangoModelFactory):
    class Meta:
        model = UserPersonalInfo
        django_get_or_create = ("user",)

    user = SubFactory(UserFactory)
    image = fake.image_url()
    first_name = fake.first_name()
    second_name = fake.last_name()
    patronymic = fake.last_name()
    email = fake.email()
