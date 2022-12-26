from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import (
    DoctorSpecialization,
    Doctor,
    User,
    DoctorDoctorSpecialization,
    UserPersonalInfo,
)
from .user_serializer import UserSerializer
from .doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from .user_personal_info_serializer import UserPersonalInfoSerializer


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

    def to_representation(
        self, instance: Doctor
    ) -> dict[User, list[DoctorSpecialization]]:
        user_from_instance = instance.user
        doctor_types = self.get_doctor_specializations(user_from_instance)
        user_personal_info = self.get_user_personal_info(user_from_instance)
        return {
            "doctor_slug": user_from_instance.slug,
            "personal_info": user_personal_info,
            "doctor_types": doctor_types,
        }

    def get_doctor_specializations(self, user: User):
        doctor_types = [
            DoctorSpecializationSerializer(
                instance=doctor_specialization.doctor_specialization
            ).data
            for doctor_specialization in DoctorDoctorSpecialization.objects.filter(
                doctor__user__pk=user.pk
            )
        ]
        return doctor_types

    def get_user_personal_info(self, user: User):
        user_personal_info = UserPersonalInfo.objects.filter(user=user).first()
        user_personal_info_data = UserPersonalInfoSerializer(
            instance=user_personal_info
        ).data
        not_neccessary_data = (
            "gender",
            "email",
            "health_status",
        )
        for key in not_neccessary_data:
            user_personal_info_data.pop(key)

        return user_personal_info_data
