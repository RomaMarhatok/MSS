import pytest
from faker import Faker
from .factories import PhysicalParametersFactory

fake = Faker()


@pytest.fixture
def factory_physical_parameters_fixture(factory_user_with_role_patient_fixture):
    return PhysicalParametersFactory.create(user=factory_user_with_role_patient_fixture)


@pytest.fixture
def physical_parameters_fixture(patient_fixture):
    return {
        "user": patient_fixture,
        "weight": fake.pyfloat(positive=True),
        "height": fake.pyfloat(positive=True),
        "pressure": fake.pyfloat(positive=True),
    }
