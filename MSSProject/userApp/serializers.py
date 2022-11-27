from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
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
from django.shortcuts import get_object_or_404


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = ("name",)


class UserSerializer(ModelSerializer):
    role = RolesSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = (
            "login",
            "password",
            "role",
        )


class UserFinderMixin:
    def get_user(self, validated_data: OrderedDict) -> User:
        user_data: OrderedDict = validated_data.pop("user")
        user = get_object_or_404(User, login=user_data["login"])
        return user


class UserPersonalInfoSerializer(ModelSerializer, UserFinderMixin):
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

    def create(self, validated_data: OrderedDict):
        user = self.get_user(validated_data)
        user_personal_info = UserPersonalInfo.objects.create(
            **validated_data, user=user
        )
        return user_personal_info


class UserDocumentSerializer(ModelSerializer, UserFinderMixin):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserDocument
        fields = (
            "user",
            "content",
        )

    def create(self, validated_data):
        user = self.get_user(validated_data)
        user_document: UserDocument = UserDocument.objects.create(
            **validated_data, user=user
        )
        return user_document


class DoctorTypesSerializer(ModelSerializer):
    class Meta:
        model = DoctorTypes
        fields = ("name",)


class DoctorSerializer(ModelSerializer, UserFinderMixin):
    user = UserSerializer(many=False, required=True)
    doctor_type = DoctorTypesSerializer(many=True, required=True)

    class Meta:
        model = Doctor
        fields = (
            "user",
            "doctor_type",
        )

    def create(self, validated_data: OrderedDict):
        user = self.get_user(validated_data)
        doctor_type_data = validated_data.pop("doctor_type")
        doctor_type = get_object_or_404(DoctorTypes, name=doctor_type_data["name"])
        doctor = Doctor.objects.create(
            **validated_data, user=user, doctor_type=doctor_type
        )
        return doctor


class PatientSerializer(ModelSerializer, UserFinderMixin):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Patient
        fields = ("user",)

    def create(self, validated_data):
        user = self.get_user(validated_data)
        patient = Patient.objects.create(user=user)
        return patient


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

    def create(self, validated_data: OrderedDict):
        doctor_data = validated_data.pop("doctor")
        patient_data = validated_data.pop("patient")
        image_data = validated_data.pop("image")
        doctor = get_object_or_404(Doctor, user__login=doctor_data["user"]["login"])
        patient = get_object_or_404(Patient, user__login=patient_data["user"]["login"])
        image = get_object_or_404(ImageForAnalyzes, pk=image_data["pk"])
        treatment_history = TreatmentsHistory.objects.create(
            **validated_data, doctor=doctor, patient=patient, image=image
        )
        return treatment_history
