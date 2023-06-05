import pytest
from datetime import datetime, timedelta
from ..models import Appointments
from .factories import AppointmentsFactory
from faker import Faker

fake = Faker(locale="ru_RU")
# factories


@pytest.fixture
def factory_appointments_fixture(
    factory_doctor_fixture,
    factory_user_with_role_patient_fixture,
    factory_doctor_specialization_fixture,
) -> Appointments:
    return AppointmentsFactory.create(
        doctor=factory_doctor_fixture,
        patient=factory_user_with_role_patient_fixture,
        doctor_specialization=factory_doctor_specialization_fixture,
    )


# dicts


@pytest.fixture
def appoitment_fixture(doctor_fixture, patient_fixture, doctor_specialization_fixture):
    return {
        "doctor": doctor_fixture,
        "patient": patient_fixture,
        "date": fake.date_time_between(
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=300),
        ),
        "doctor_specialization": doctor_specialization_fixture,
    }
