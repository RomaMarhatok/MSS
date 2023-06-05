from django.conf import settings
from factory import SubFactory
from faker import Faker
from factory.django import DjangoModelFactory
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.storages.filesystem import FileSystemStorage
from ..models import Document, DocumentType, FileDocument
from user.tests.factories import UserFactory
from doctor.tests.factories import DoctorFactory

FAKER = Faker(locale="ru_RU")
FS_STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT)


class DocumentTypeFactory(DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = FAKER.pystr()


class DocumentFactory(DjangoModelFactory):
    class Meta:
        model = Document

    content = FAKER.text(max_nb_chars=10000)
    name = FAKER.pystr()
    user = SubFactory(UserFactory)
    creator = SubFactory(DoctorFactory)
    document_type = SubFactory(DocumentTypeFactory)


class FileDocumentFactory(DjangoModelFactory):
    class Meta:
        model = FileDocument

    user = SubFactory(UserFactory)
    creator = SubFactory(DoctorFactory)
    document_type = SubFactory(DocumentTypeFactory)
    document = DocxFileProvider(FAKER).docx_file(storage=FS_STORAGE)
