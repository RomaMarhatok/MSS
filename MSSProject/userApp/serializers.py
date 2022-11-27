from rest_framework.serializers import ModelSerializer

from .models import (
    Doctor,
    DoctorTypes,
    ImageForAnalyzes,
    Patient,
    Roles,
    TreatmentsHistory,
    User,
    UserDocument,
    UserPersonalInfo,
)


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = ("name",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "login",
            "password",
            "role",
        )


class UserPersonalInfoSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserPersonalInfo
        fields = (
            "user",
            "image",
            "first_name",
            "second_name",
            "patronymic",
            "email",
        )


class UserDocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserDocument
        fields = (
            "user",
            "content",
        )


class DoctorTypesSerializer(ModelSerializer):
    class Meta:
        model = DoctorTypes
        fields = ("name",)


class DoctorSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)
    doctor_type = DoctorTypesSerializer(many=True, required=True)

    class Meta:
        model = Doctor
        fields = (
            "user",
            "doctor_type",
        )


class PatientSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Patient
        fields = ("user",)


class ImageForAnlyzesSerializer(ModelSerializer):
    class Meta:
        model = ImageForAnalyzes
        fields = (
            "image",
            "description",
        )


class TreatmenstHistorySerializer(ModelSerializer):
    doctor = DoctorSerializer(many=False, required=True)
    patient = PatientSerializer(many=False, required=True)
    image = ImageForAnlyzesSerializer(many=True, required=True)

    class Meta:
        model = TreatmentsHistory
        fields = (
            "description",
            "doctor",
            "patient",
            "image",
        )
