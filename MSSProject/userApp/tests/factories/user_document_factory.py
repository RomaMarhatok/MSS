from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ...models import UserDocument
from ..factories.document_type_factory import DocumentTypeFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class UserDocumentFactory(DjangoModelFactory):
    class Meta:
        model = UserDocument

    content = fake.pystr()
    doctype = SubFactory(DocumentTypeFactory)
    user = SubFactory(UserFactory)
