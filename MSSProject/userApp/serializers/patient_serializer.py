from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .doctor_serializer import UserSerializer
from ..models import Patient, User


class PatientSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Patient
        fields = ("user",)
        extra_kwargs = {"user": {"validators": []}}

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(login=validated_data["user"]["login"])
        return Patient.objects.create(user=user)
