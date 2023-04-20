import pytest
from django.urls import reverse
from django.test.client import Client
from document.models import Document
from document.serializers import DocumentSerializer
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_document_fixture):
    token = Token.objects.create(user=factory_document_fixture.creator.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    serializer = DocumentSerializer(instance=factory_document_fixture)
    serializer.data.pop("content")
    data = {
        "document_slug": factory_document_fixture.slug,
        "content": "test",
        **serializer.data,
    }
    url = reverse("update-user-document")
    response = client.post(url, data, **headers)
    document = Document.objects.first()
    assert response.status_code == 200
    assert bool(response.json())
    assert Document.objects.count() == 1
    assert document.content == "test"
