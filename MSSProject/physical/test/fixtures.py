import pytest
import random
from .factories import PhysicalParametersFactory


@pytest.fixture
def factory_physical_parameters_fixture(factory_user_with_role_patient_fixture):
    return PhysicalParametersFactory.create(user=factory_user_with_role_patient_fixture)


@pytest.fixture
def physical_parameters_fixture(patient_fixture):
    return {
        "user": patient_fixture,
        "weight": round(random.uniform(60, 300), 2),
        "height": round(random.uniform(100, 250), 2),
        "pressure": round(random.uniform(60, 250), 2),
    }
