from datetime import datetime
from django.db import models
from ..utils.string_utls import generate_hash_from_string
from ..services.image_service import ImageService


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


image_service = ImageService()


class ImageForAnalyzes(models.Model):
    image = models.ImageField(
        "image for analyzes",
        upload_to=media_path_builder_for_analyzes_images,
        null=True,
        blank=True,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = generate_hash_from_string(self.description[:10]) + ".jpg"
        super(ImageForAnalyzes, self).save(*args, **kwargs)
        if self.image:
            image_service.resize_image(self.image.path)

    class Meta:
        db_table = "image_for_analyzes"
