from django.db import models


class Roles(models.Model):
    name = models.CharField("role name", max_length=100, unique=True)


class User(models.Model):
    username = models.CharField("user name", max_length=100, unique=True)
    login = models.CharField("user login", max_length=100)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField("user image", upload_to="")
    first_name = models.CharField("first name", max_length=100)
    second_name = models.CharField("second name", max_length=100)
    patronymic = models.CharField("patronymic", max_length=100, blank=True)
    email = models.EmailField("email", max_length=100)


class UserDocument(models.Model):
    content = models.TextField("document content")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DoctorTypes(models.Model):
    doctor_type = models.CharField(
        "doctor profession name", max_length=100, unique=True
    )


class Doctors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_type = models.ForeignKey(DoctorTypes, on_delete=models.SET_NULL, null=True)


class Patients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ImageForAnalyzes(models.Model):
    image = models.ImageField()
    description = models.TextField()


class TreatmentsHistory(models.Model):
    description = models.TextField()
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
