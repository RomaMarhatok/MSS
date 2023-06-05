from datetime import datetime
from django.db import models
from common.utils.string_utils import generate_hash_from_string, generate_slug_from_str


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
    slug = models.SlugField(unique=True, max_length=1000)
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
        ext = self.image.name.split(".")[1]
        old_name = self.image.name.split(".")[0]
        self.slug = generate_slug_from_str(generate_hash_from_string(old_name))
        self.image.name = generate_hash_from_string(old_name) + "." + ext
        super(ImageForAnalyzes, self).save(*args, **kwargs)

    class Meta:
        db_table = "image_for_analyzes"
        verbose_name = "Изображение для анализа"
        verbose_name_plural = "Изображения для анализа"

    def __str__(self) -> str:
        return self.pk + " " + self.image.name
