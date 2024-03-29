from datetime import datetime, timedelta
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from common.utils.image_utils import load_image_from_url
from ..models import (
    ImageForAnalyzes,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
    TreatmentHistoryDocument,
)

# doctor app imports
from doctor.tests.factories import DoctorFactory

# user app imports
from user.tests.factories import UserFactory
from document.tests.factories import DocumentFactory

fake = Faker(locale="ru_RU")


class ImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = ImageForAnalyzes

    image = load_image_from_url(fake.image_url())
    description = fake.text(max_nb_chars=10000)


class TreatmentHistoryFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistory

    title = fake.text(max_nb_chars=10)
    short_description = fake.text(max_nb_chars=100)
    description = fake.text(max_nb_chars=1000)
    conclusion = fake.text(max_nb_chars=1000)
    date = fake.date_time_between(
        start_date=datetime.now(), end_date=datetime.now() + timedelta(days=300)
    )
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(UserFactory)


class TreatmentHistoryImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes

    treatment_history = SubFactory(TreatmentHistoryFactory)
    image_for_analyzes = SubFactory(ImageForAnalyzesFactory)


class TreatmentHistoryDocumentFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryDocument

    treatment_history = SubFactory(TreatmentHistoryFactory)
    document = SubFactory(DocumentFactory)
