from datetime import datetime, timedelta
from factory import SubFactory
from factory.django import DjangoModelFactory
from ..models import Appointments
from faker import Faker

# user app imports
from user.tests.factories import UserFactory

# doctor app imports
from doctor.tests.factories import DoctorFactory, DoctorSpecializationFactory

fake = Faker()


class AppointmentsFactory(DjangoModelFactory):
    class Meta:
        model = Appointments

    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(UserFactory)
    doctor_specialization = SubFactory(DoctorSpecializationFactory)
    date = fake.date_time_between(
        start_date=datetime.now(), end_date=datetime.now() + timedelta(days=300)
    )
