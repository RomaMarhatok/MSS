import pytest
from django.urls import reverse
from django.test.client import Client

client = Client()


@pytest.mark.django_db
def test():
    url = reverse("doctor-types-list")
    response = client.get(url)
    assert response.status_code == 200
    assert bool(response.json())
