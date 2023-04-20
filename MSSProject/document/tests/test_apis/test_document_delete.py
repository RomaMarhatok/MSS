import pytest
from django.db.models import Q
from django.urls import reverse
from django.test.client import Client
from document.models import Document
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_document_fixture):
    token = Token.objects.create(user=factory_document_fixture.creator.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "document_slug": factory_document_fixture.slug,
        "creator_slug": factory_document_fixture.creator.user.slug,
    }
    url = reverse("doctor-delete-document")
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert Document.objects.count() == 0


@pytest.mark.django_db
def test_bad(factory_document_fixture):
    token = Token.objects.create(user=factory_document_fixture.creator.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "document_slug": "not-exist",
        "creator_slug": "not-exist",
    }
    url = reverse("doctor-delete-document")
    response = client.post(url, data, **headers)
    assert response.status_code == 400
    assert bool(response.json())
    assert Document.objects.count() == 1
