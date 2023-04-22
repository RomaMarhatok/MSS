from common.utils.file_utils import generate_fake_file
from django.core.files.uploadedfile import InMemoryUploadedFile


def test():
    doc = generate_fake_file()
    assert isinstance(doc, InMemoryUploadedFile)
