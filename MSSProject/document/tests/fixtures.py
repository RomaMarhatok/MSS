import pytest
import random
from ..models import DocumentType, Document
from .factories import DocumentTypeFactory, DocumentFactory
from faker import Faker

fake = Faker()
# factories


@pytest.fixture
def factory_document_type_fixture() -> DocumentType:
    return DocumentTypeFactory.create()


@pytest.fixture
def factory_document_fixture(
    factory_user_with_role_patient_fixture,
    factory_document_type_fixture,
    factory_doctor_fixture,
) -> Document:
    return DocumentFactory.create(
        user=factory_user_with_role_patient_fixture,
        document_type=factory_document_type_fixture,
        creator=factory_doctor_fixture,
    )


# dicts
@pytest.fixture
def document_type_fixture() -> dict:
    return {
        "name": random.choice(DocumentType.DOCUMENT_TYPE_CHOICES)[0],
    }


@pytest.fixture
def document_fixture(patient_fixture, document_type_fixture, doctor_fixture) -> dict:
    return {
        "name": fake.pystr(),
        "content": fake.text(max_nb_chars=10000),
        "user": patient_fixture,
        "document_type": document_type_fixture,
        "creator": doctor_fixture,
    }
