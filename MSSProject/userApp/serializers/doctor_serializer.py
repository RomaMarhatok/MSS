from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import DoctorType, Doctor, User, DoctorDoctorTypes, UserPersonalInfo
from .user_serializer import UserSerializer
from .doctor_type_serializer import DoctorTypeSerializer
from .user_serializer import UserPersonalInfoSerializer


class DoctorSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Doctor
        fields = ("user",)
        extra_kwargs = {
            "user": {"validators": []},
            "url": {"lookup_field": "user"},
        }

    def create(self, validated_data: OrderedDict) -> Doctor:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = Doctor.objects.get_or_create(user=user)
        return instance

    def to_representation(self, instance: Doctor) -> dict[User, list[DoctorType]]:
        user_from_instance = instance.user
        doctor_types = [
            DoctorTypeSerializer(instance=doctor_doctor_type.doctor_type).data
            for doctor_doctor_type in DoctorDoctorTypes.objects.filter(
                doctor__user__pk=user_from_instance.pk
            )
        ]
        user_personal_info = UserPersonalInfo.objects.filter(
            user=user_from_instance
        ).first()
        user_personal_info_data = UserPersonalInfoSerializer(
            instance=user_personal_info
        ).data
        extracted_data = {
            "first_name": user_personal_info_data["first_name"],
            "second_name": user_personal_info_data["second_name"],
            "patronymic": user_personal_info_data["patronymic"],
            "gender": user_personal_info_data["gender"],
            "age": user_personal_info_data["age"],
        }
        return {"personal_info": extracted_data, "doctor_types": doctor_types}
