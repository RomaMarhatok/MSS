import pytest
import random
from common.utils.file_utils import generate_fake_file
from ..models import DocumentType, Document
from .factories import DocumentTypeFactory, DocumentFactory, FileDocumentFactory
from ..enums import BaseDocumentTypesEnum
from faker import Faker

FAKER = Faker(locale="ru_RU")
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


@pytest.fixture
def factory_file_document_fixture(
    factory_user_with_role_patient_fixture,
    factory_document_type_fixture,
    factory_doctor_fixture,
) -> FileDocumentFactory:
    return FileDocumentFactory.create(
        user=factory_user_with_role_patient_fixture,
        document_type=factory_document_type_fixture,
        creator=factory_doctor_fixture,
    )


# dicts
@pytest.fixture
def document_type_fixture() -> dict:
    return {
        "name": random.choice(
            [
                BaseDocumentTypesEnum.TEST.value,
                BaseDocumentTypesEnum.ANALYZE.value,
                BaseDocumentTypesEnum.CONCLUSION.value,
            ]
        ),
    }


@pytest.fixture
def document_fixture(patient_fixture, document_type_fixture, doctor_fixture) -> dict:
    return {
        "name": FAKER.pystr(),
        "content": FAKER.text(max_nb_chars=10000),
        "user": patient_fixture,
        "document_type": document_type_fixture,
        "creator": doctor_fixture,
    }


@pytest.fixture
def file_document_fixture(patient_fixture, document_type_fixture, doctor_fixture):
    return {
        "document": generate_fake_file(),
        "user": patient_fixture,
        "document_type": document_type_fixture,
        "creator": doctor_fixture,
    }
