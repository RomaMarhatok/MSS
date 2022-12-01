from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .doctor_serializer import UserSerializer
from ..models import Patient, User


class PatientSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Patient
        fields = ("user",)
        extra_kwargs = {
            "user": {"validators": []},
            "url": {"lookup_field": "user"},
        }

    def create(self, validated_data: OrderedDict) -> Patient:
        user = User.objects.get(login=validated_data["user"]["login"])
        instance, _ = Patient.objects.get_or_create(user=user)
        return instance
