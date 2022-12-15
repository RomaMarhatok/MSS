from __future__ import annotations
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from .utils.slug_utils import generate_slug_from_str
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models import Q


class Role(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField("role name", max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Role, self).save(*args, **kwargs)

    class Meta:
        db_table = "role"


class User(AbstractUser):
    slug = models.SlugField(max_length=100, unique=True)
    login = models.CharField("user login", max_length=100, unique=True)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.login)
        self.username = self.login
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = "user"

    @staticmethod
    def is_exist(login: str, password: str) -> bool:
        return User.objects.filter(Q(login=login) & Q(password=password)).exists()

    @staticmethod
    def get_user_by_token(token: str) -> User:
        return Token.objects.filter(key=token).first().user

    @staticmethod
    def get_user_by_login(login: str) -> User:
        return User.objects.filter(login=login).first()


def media_path_builder_for_user_info(instance, filename):
    now_date = datetime.now().strftime("%Y/%m/%d")
    if hasattr(instance, "user"):
        return "/".join(
            [
                "media_files",
                "user_info",
                instance.user.login,
                now_date,
                filename,
            ]
        )


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        "user image", upload_to=media_path_builder_for_user_info, null=True, blank=True
    )
    first_name = models.CharField("first name", max_length=100)
    second_name = models.CharField("second name", max_length=100)
    patronymic = models.CharField("patronymic", max_length=100, blank=True)
    email = models.EmailField("email", max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.login

    class Meta:
        db_table = "user_personal_info"


class UserDocumentType(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(UserDocumentType, self).save(*args, **kwargs)

    class Meta:
        db_table = "user_document_type"


class UserDocument(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    content = models.TextField("document content")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.ForeignKey(
        UserDocumentType, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "user_document"

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(UserDocument, self).save(*args, **kwargs)


class DoctorType(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    doctor_type = models.CharField(
        "doctor profession name", max_length=100, unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.doctor_type)
        return super(DoctorType, self).save(*args, **kwargs)

    class Meta:
        db_table = "doctor_type"


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"


class DoctorDoctorTypes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_type = models.ForeignKey(DoctorType, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor_doctor_type"


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"


def media_path_builder_for_analyzes_images(instance, filename):
    now_date = datetime.now().strftime("%Y/%m/%d")
    return "/".join(
        [
            "media_files",
            "anylez_images",
            now_date,
            filename,
        ]
    )


class ImageForAnalyzes(models.Model):
    image = models.ImageField(
        "image for analyzes",
        upload_to=media_path_builder_for_analyzes_images,
        null=True,
        blank=True,
    )
    description = models.TextField()

    class Meta:
        db_table = "image_for_analyzes"


class TreatmentHistory(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(
            self.patient.user.login
        ) + generate_slug_from_str(self.doctor.user.login)
        return super(TreatmentHistory, self).save(*args, **kwargs)

    class Meta:
        db_table = "treatment_history"


class TreatmentHistoryImageForAnalyzes(models.Model):
    treatment_history = models.ForeignKey(TreatmentHistory, on_delete=models.CASCADE)
    image_for_analyzes = models.ForeignKey(ImageForAnalyzes, on_delete=models.CASCADE)

    class Meta:
        db_table = "treatment_history_image_for_analyzes"
