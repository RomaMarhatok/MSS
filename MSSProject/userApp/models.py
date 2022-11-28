from django.db import models


def content_product_file_path(instance, filename):
    return "/".join(["products", instance.pk, "%Y", "%m", "%d", filename])


class Roles(models.Model):
    name = models.CharField("role name", max_length=100, unique=True)


class User(models.Model):
    login = models.CharField("user login", max_length=100, unique=True)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        "user image", upload_to=content_product_file_path, null=True, blank=True
    )
    first_name = models.CharField("first name", max_length=100)
    second_name = models.CharField("second name", max_length=100)
    patronymic = models.CharField("patronymic", max_length=100, blank=True)
    email = models.EmailField("email", max_length=100)


class UserDocument(models.Model):
    content = models.TextField("document content")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DoctorType(models.Model):
    doctor_type = models.CharField(
        "doctor profession name", max_length=100, unique=True
    )


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_type = models.ForeignKey(DoctorType, on_delete=models.SET_NULL, null=True)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ImageForAnalyzes(models.Model):
    image = models.ImageField(
        "user image", upload_to=content_product_file_path, null=True, blank=True
    )
    description = models.TextField()


class TreatmentHistory(models.Model):
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(ImageForAnalyzes, on_delete=models.SET_NULL, null=True)
