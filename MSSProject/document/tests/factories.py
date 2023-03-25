from factory import SubFactory
from factory.django import DjangoModelFactory
from ..models import Document, DocumentType
from faker import Faker

# user app import
from user.tests.factories import UserFactory

# doctor app import
from doctor.tests.factories import DoctorFactory

fake = Faker()


class DocumentTypeFactory(DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = fake.pystr()


class DocumentFactory(DjangoModelFactory):
    class Meta:
        model = Document

    content = fake.text(max_nb_chars=10000)
    name = fake.pystr()
    user = SubFactory(UserFactory)
    creator = SubFactory(DoctorFactory)
    document_type = SubFactory(DocumentTypeFactory)
