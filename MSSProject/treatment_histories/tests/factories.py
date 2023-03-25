from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from common.utils.image_utils import load_image_from_url
from ..models import (
    ImageForAnalyzes,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
)

# doctor app imports
from doctor.tests.factories import DoctorFactory

# user app imports
from user.tests.factories import UserFactory

fake = Faker()


class ImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = ImageForAnalyzes

    image = load_image_from_url(fake.image_url())
    description = fake.text(max_nb_chars=10000)


class TreatmentHistoryFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistory

    title = fake.text(max_nb_chars=100)
    short_description = fake.text(max_nb_chars=1000)
    description = fake.text(max_nb_chars=10000)
    conclusion = fake.text(max_nb_chars=10000)
    date = fake.date_time()
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(UserFactory)


class TreatmentHistoryImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes

    treatment_history = SubFactory(TreatmentHistoryFactory)
    image_for_analyzes = SubFactory(ImageForAnalyzesFactory)
