from dataclasses import dataclass
from ...repositories.document_repository import DocumentRepository


@dataclass
class DocumentService:
    document_repository: DocumentRepository = DocumentRepository()

    def get_document_info(self, document_slug: str, user_slug: str):
        document = self.document_repository.get_document_by(
            serialized=True, document_slug=document_slug, user_slug=user_slug
        )
        creator = self.document_repository.get_document_creator(
            document.get("slug", None)
        )
        document.update({"creator": {"slug": creator.user.slug}})
        return {
            "document": document,
        }

    def get_all_documents_with_content(self, user_slug: str):
        return self.document_repository.get_all_user_documents(
            user_slug, serialized=True, include_context=True
        )

    def get_all_documents_without_content(self, user_slug: str):
        return self.document_repository.get_all_user_documents(
            user_slug, serialized=True, include_context=False
        )
