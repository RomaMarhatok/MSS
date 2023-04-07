import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token

from doctor.serializers import DoctorDoctorSpecializationSerializer

client = Client()


@pytest.mark.django_db
def test(factory_treatment_history_fixture, factory_doctor_specialization_fixture):
    patient_slug = factory_treatment_history_fixture.patient.slug

    serializer = DoctorDoctorSpecializationSerializer(
        data={
            "doctor": factory_treatment_history_fixture.doctor.pk,
            "doctor_specialization": factory_doctor_specialization_fixture.pk,
        }
    )
    assert serializer.is_valid()
    serializer.save()

    doctor_specialization_slug = (
        factory_treatment_history_fixture.doctor.doctor_doctor_specialization.first().doctor_specialization.slug
    )
    url = reverse(
        "treatment-history-list",
        args=[patient_slug, doctor_specialization_slug],
    )
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    url = reverse(
        "treatment-history-list", args=[patient_slug, doctor_specialization_slug]
    )
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())
