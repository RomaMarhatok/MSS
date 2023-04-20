import os

import pytest
from common.utils.image_utils import FolderController, load_image_from_url
from faker import Faker

# from treatment.models import UserPersonalInfo
from treatment_histories.models import ImageForAnalyzes

fake = Faker()


@pytest.mark.django_db
def test():
    image_url = fake.image_url()
    img = load_image_from_url(image_url)
    ImageForAnalyzes.objects.create(image=img, description="description")

    assert ImageForAnalyzes.objects.count() == 1
    assert os.path.isdir(os.getcwd() + "\\media")
    folder_controller = FolderController()
    folder_controller.remove_dir("media")
