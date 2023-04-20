import pytest
from django.urls import reverse
from django.test.client import Client
from document.models import Document, DocumentType
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(
    factory_user_with_role_patient_fixture,
    factory_doctor_fixture,
    document_fixture,
    document_type_fixture,
):
    dt = DocumentType.objects.create(name=document_type_fixture["name"])
    user_slug = factory_user_with_role_patient_fixture.slug
    creator_slug = factory_doctor_fixture.user.slug
    document_fixture.pop("document_type")
    data = {
        "name": document_fixture["name"],
        "content": document_fixture["content"],
        "document_type_slug": dt.slug,
        "user_slug": user_slug,
        "creator_slug": creator_slug,
    }
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    url = reverse("create-user-document")
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert Document.objects.count() == 1
