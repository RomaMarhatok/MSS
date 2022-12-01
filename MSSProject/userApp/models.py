from datetime import datetime
from django.db import models


class Role(models.Model):
    name = models.CharField("role name", max_length=100, unique=True)


class User(models.Model):
    login = models.CharField("user login", max_length=100, unique=True)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


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
    email = models.EmailField("email", max_length=100)

    def __str__(self) -> str:
        return self.user.login


class UserDocument(models.Model):
    content = models.TextField("document content")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DoctorType(models.Model):
    doctor_type = models.CharField(
        "doctor profession name", max_length=100, unique=True
    )


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DoctorDoctorTypes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_type = models.ForeignKey(DoctorType, on_delete=models.CASCADE)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


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
        "image for anlayzes",
        upload_to=media_path_builder_for_analyzes_images,
        null=True,
        blank=True,
    )
    description = models.TextField()


class TreatmentHistory(models.Model):
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)


class TreatmentHistoryImageForAnalyzes(models.Model):
    treatment_history = models.ForeignKey(TreatmentHistory, on_delete=models.CASCADE)
    image_for_analyzes = models.ForeignKey(ImageForAnalyzes, on_delete=models.CASCADE)
