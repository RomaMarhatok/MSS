import pytest
import os
from userApp.utils.image_utils import load_image_from_url, FolderController
from faker import Faker
from userApp.models import UserPersonalInfo

fake = Faker()


@pytest.mark.django_db
def test(factory_user_fixture, user_personal_info_fixture):
    image_url = fake.image_url()
    img = load_image_from_url(image_url)
    first_name = user_personal_info_fixture["first_name"]
    second_name = user_personal_info_fixture["second_name"]
    UserPersonalInfo.objects.create(
        user=factory_user_fixture,
        first_name=first_name,
        second_name=second_name,
        image=img,
    )
    assert UserPersonalInfo.objects.count() == 1
    assert os.path.isdir(os.getcwd() + "\\media")
    folder_controller = FolderController()
    folder_controller.remove_dir("media")
