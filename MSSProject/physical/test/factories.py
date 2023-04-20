from factory.django import DjangoModelFactory
from factory import SubFactory
from ..models import PhysicalParameters
from user.tests.factories import UserFactory
from faker import Faker

fake = Faker()


class PhysicalParametersFactory(DjangoModelFactory):
    class Meta:
        model = PhysicalParameters

    user = SubFactory(UserFactory)
    weight = fake.pyfloat(positive=True, min_value=60.0)
    height = fake.pyfloat(positive=True, min_value=100.0)
    pressure = fake.pyfloat(positive=True, min_value=120.0)
