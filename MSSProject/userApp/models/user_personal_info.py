from datetime import datetime
from django.db import models
from ..utils.string_utls import generate_hash_from_string
from .user import User


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
    gender = models.CharField(max_length=150, blank=True, default="Other")
    age = models.IntegerField(blank=True, default=-1)
    health_status = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.user.login

    class Meta:
        db_table = "user_personal_info"

    def save(self, *args, **kwargs) -> None:
        self.image.name = (
            generate_hash_from_string(f"{self.first_name} {self.second_name}") + ".jpg"
        )
        return super(UserPersonalInfo, self).save(*args, **kwargs)
