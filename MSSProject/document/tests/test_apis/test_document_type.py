import pytest
from django.test import Client
from django.urls import reverse

client = Client()


@pytest.mark.django_db
def test():
    url = reverse("list-document-types")
    response = client.get(url)
    print(response.json())
    assert response.status_code == 200
    assert bool(response.json())
