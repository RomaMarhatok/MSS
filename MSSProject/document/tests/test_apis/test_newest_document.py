import pytest
from django.test.client import Client
from django.urls import reverse
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_document_fixture):
    url = reverse("newest-patient-document", args=[factory_document_fixture.user.slug])
    token = Token.objects.create(user=factory_document_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())


@pytest.mark.django_db
def test_bad(factory_document_fixture):
    url = reverse("newest-patient-document", args=["not-exist-slug"])
    token = Token.objects.create(user=factory_document_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 404
    assert bool(response.json())
