from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ...models import DocumentType
from ..factories.document_type_factory import DocumentTypeFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class UserDocument(DjangoModelFactory):
    class Meta:
        model = DocumentType

    content = fake.pystr()
    doctype = SubFactory(DocumentTypeFactory)
    user = SubFactory(UserFactory)
