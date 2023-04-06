from __future__ import annotations
from django.db import models
from datetime import datetime
from PIL import Image
from common.utils.string_utils import generate_hash_from_string
from .user import User


def media_path_builder_for_user_info(instance: UserPersonalInfo, filename):
    now_date = datetime.now().strftime("%Y/%m/%d")
    if hasattr(instance, "user"):
        return "/".join(
            [
                "media_files",
                "user_info",
                instance.user.slug,
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

    class Meta:
        db_table = "user_personal_info"

    def save(self, *args, **kwargs) -> None:
        if self.image:
            self.image.name = (
                generate_hash_from_string(f"{self.first_name} {self.second_name}")
                + ".jpg"
            )
        super(UserPersonalInfo, self).save(*args, **kwargs)
        # if self.image:
        #     img = Image.open(self.image.path).convert("RGB")
        #     img = img.resize((340, 300), Image.Resampling.LANCZOS)
        #     img.save(self.image.path)

    def __str__(self) -> str:
        return self.first_name + " " + self.second_name + " " + self.patronymic

    @property
    def full_name(self):
        return self.first_name + " " + self.second_name + " " + self.patronymic
