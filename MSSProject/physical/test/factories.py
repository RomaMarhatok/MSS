import random
from factory.django import DjangoModelFactory
from factory import SubFactory
from ..models import PhysicalParameters
from user.tests.factories import UserFactory


class PhysicalParametersFactory(DjangoModelFactory):
    class Meta:
        model = PhysicalParameters

    user = SubFactory(UserFactory)
    weight = round(random.uniform(60, 300), 2)
    height = round(random.uniform(100, 250), 2)
    pressure = round(random.uniform(60, 250), 2)
