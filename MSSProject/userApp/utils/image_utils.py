import requests
import os
import shutil
from django.core.files.images import ImageFile
from PIL import Image
from io import BytesIO
from dataclasses import dataclass
from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class Client:
    @staticmethod
    def get(url):
        with requests.get(url, stream=True) as resp:
            return resp.content


@dataclass
class FolderController:
    project_root = os.getcwd()

    def remove_file(self, related_path_folder):
        path = self.project_root + "\\" + related_path_folder
        if os.path.isfile(path):
            os.remove(path)

    def remove_dir(self, related_path_to_folder):
        path = self.project_root + "\\" + related_path_to_folder
        if os.path.isdir(path):
            shutil.rmtree(path)

    def create_dir(self, path_to_dir):
        if not os.path.exists(path_to_dir):
            os.makedirs(path_to_dir)


def load_image_from_url_to_file(
    image_url, path_to_folder="userApp\\tests\\test_images", file_name="test_image.png"
) -> ImageFile | bool:

    resp_content = Client.get(image_url)
    pil_image = Image.open(BytesIO(resp_content))

    path_to_loaded_file = path_to_folder + "\\" + file_name
    folder_controller = FolderController()

    folder_controller.create_dir(path_to_folder)
    folder_controller.remove_file(path_to_loaded_file)

    pil_image.save(path_to_loaded_file)

    img = ImageFile(open(path_to_loaded_file, "rb"), file_name)
    yield img
    img.close()

    folder_controller.remove_file(path_to_loaded_file)
    folder_controller.remove_dir("media")
    folder_controller.remove_dir(path_to_folder)

    yield True


def load_image_from_url(image_url):
    resp_content = Client.get(image_url)
    pil_image = Image.open(BytesIO(resp_content)).convert("RGB")
    img_io = BytesIO()
    pil_image.save(img_io, format="JPEG")
    return InMemoryUploadedFile(
        img_io,
        field_name=None,
        name="token" + ".jpg",
        content_type="image/jpeg",
        size=img_io.tell,
        charset=None,
    )
