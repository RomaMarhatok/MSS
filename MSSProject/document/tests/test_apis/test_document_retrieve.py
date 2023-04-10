import pytest
from django.urls import reverse
from django.test.client import Client

from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_document_fixture):
    doc_slug = factory_document_fixture.slug
    user_slug = factory_document_fixture.user.slug
    url = reverse("retrieve-user-document", args=[user_slug, doc_slug])
    token = Token.objects.create(user=factory_document_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200


@pytest.mark.django_db
def test_bad(factory_document_fixture):
    url = reverse("retrieve-user-document", args=["not-exist-slug", "not-exist-slug"])
    token = Token.objects.create(user=factory_document_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 400
