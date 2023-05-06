import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from treatment_histories.models import TreatmentHistory, TreatmentHistoryDocument
from document.models import Document

client = Client()


@pytest.mark.django_db
def test(factory_treatment_history_fixture, factory_document_fixture):
    url = reverse("add-document-treatment_history")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    data = {
        "treatment_history_slug": factory_treatment_history_fixture.slug,
        "document_slug": factory_document_fixture.slug,
    }
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert TreatmentHistory.objects.count() == 1
    assert Document.objects.count() == 1
    assert TreatmentHistoryDocument.objects.count() == 1


@pytest.mark.django_db
def test_treatment_history_slug(
    factory_treatment_history_fixture, factory_document_fixture
):
    url = reverse("add-document-treatment_history")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    data = {
        "treatment_history_slug": "not-exist",
        "document_slug": factory_document_fixture.slug,
    }
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert TreatmentHistory.objects.count() == 1
    assert Document.objects.count() == 1
    assert TreatmentHistoryDocument.objects.count() == 0


@pytest.mark.django_db
def test_document_slug(factory_treatment_history_fixture, factory_document_fixture):
    url = reverse("add-document-treatment_history")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    data = {
        "treatment_history_slug": factory_treatment_history_fixture.slug,
        "document_slug": "not-exist",
    }
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert TreatmentHistory.objects.count() == 1
    assert Document.objects.count() == 1
    assert TreatmentHistoryDocument.objects.count() == 0
