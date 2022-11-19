from django.db import models


class User(models.Model):
    username = models.CharField("user name", max_length=100, unique=True)
    login = models.CharField("user login", max_length=100)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey("Roles", on_delete=models.SET_NULL, null=True)


class Roles(models.Model):
    name = models.CharField("role name", max_length=100, unique=True)


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField("user image", upload_to="")
    first_name = models.CharField("first name", max_length=100)
    second_name = models.CharField("second name", max_length=100)
    patronymic = models.CharField("patronymic", max_length=100, blank=True)
    email = models.EmailField("email", max_length=100)


class DocumentType(models.Model):
    document_type = models.CharField("document type", max_length=20)


class UserDocument(models.Model):
    content = models.TextField("document content")
    doctype = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
