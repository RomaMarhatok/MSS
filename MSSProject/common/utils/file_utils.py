from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from faker import Faker
from faker_file.providers.docx_file import DocxFileProvider

FAKER = Faker()


def generate_fake_file() -> InMemoryUploadedFile:
    content = FAKER.text(max_nb_chars=10000)
    doc_bytes = DocxFileProvider(FAKER).docx_file(content=content, raw=True)
    doc_io = BytesIO(doc_bytes)
    doc_io.seek(0)
    return InMemoryUploadedFile(
        doc_io,
        field_name=None,
        name=FAKER.file_name(extension="docx"),
        content_type="msword",
        size=doc_io.tell,
        charset=None,
    )
