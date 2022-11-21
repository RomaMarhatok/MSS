from factory.django import DjangoModelFactory
from faker import Faker

from ...models import DocumentType

fake = Faker()


class DocumentTypeFactory(DjangoModelFactory):
    class Meta:
        model = DocumentType

    document_type = fake.pystr()
