from django.http import JsonResponse, HttpResponse
from django.db import transaction
from rest_framework import exceptions
from ..serializers import TreatmentHistorySerializer, ImageForAnlyzeSerializer
from .base.base_treatment_history_service import BaseTreatmentHistoryService
from user.serializers import UserPersonalInfoSerializer
from document.serializers import DocumentSerializer
from document.models import Document


class DoctorTreatmentHistoryService(BaseTreatmentHistoryService):
    def get_patient_treatment_histories_list(
        self, patient_slug: str, doctor_specialization_slug: str, request=None
    ) -> JsonResponse:
        if self.is_user_exist(patient_slug):
            print("USER EXIST")
            user = self.user_repository.get(slug=patient_slug)
        treatments_histories = self.list(
            patient_slug,
            doctor_specialization_slug=doctor_specialization_slug,
            request=request,
        )
        print(treatments_histories)
        patient_info = (
            UserPersonalInfoSerializer(instance=user.userpersonalinfo).data
            if hasattr(user, "userpersonalinfo")
            else {}
        )
        return JsonResponse(
            data={
                "patient_info": patient_info,
                "treatment_histories": treatments_histories,
            }
        )

    def get_patient_treatment_history(self, treatment_history_slug: str, request):
        return JsonResponse(
            data=self.get(treatment_history_slug, request),
        )

    @transaction.atomic
    def create_treatment_history(self, data: dict):
        treatment_history = self.treatment_history_repository.create(data)
        treatment_history_serializer = TreatmentHistorySerializer(
            instance=treatment_history
        )
        return JsonResponse(
            data={
                "treatment_history": treatment_history_serializer.data,
                "images_for_analyzes": [],
                "documents": [],
            },
        )

    @transaction.atomic
    def create_image_for_analyzes(self, data: dict, request=None):
        treatment_history_slug = data.get("treatment_history_slug", None)
        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        image_for_analyzes = self.image_for_analyzes_repository.create(data)
        self.treatment_history_image_for_analyzes_repository.create(
            treatment_history, image_for_analyzes
        )
        image_for_analyzes_serializer = ImageForAnlyzeSerializer(
            instance=image_for_analyzes, context={"request": request}
        )
        return JsonResponse(
            data={
                "image_for_analyze": image_for_analyzes_serializer.data,
            }
        )

    @transaction.atomic
    def update_treatment_history(self, data: dict):
        treatment_history_slug = data.get("treatment_history_slug", None)
        if not self.treatment_history_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                }
            )
        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        updated_treatment_history = self.treatment_history_repository.update(
            data, treatment_history
        )
        treatment_history_serializer = TreatmentHistorySerializer(
            instance=updated_treatment_history
        )
        return JsonResponse(
            data={
                "treatment_history": treatment_history_serializer.data,
            }
        )

    @transaction.atomic
    def delete_image_for_analyzes(self, data: dict):
        treatment_history_slug = data.get("treatment_history_slug", None)
        image_for_analyzes_slug = data.get("image_for_analyzes_slug", None)
        treatment_history_image_for_analyzes = (
            self.treatment_history_image_for_analyzes_repository.get(**data)
        )
        treatment_history_image_for_analyzes.image_for_analyzes.delete()
        return JsonResponse(
            data={
                "treatment_history_slug": treatment_history_slug,
                "deleted_image_slug": image_for_analyzes_slug,
            }
        )

    @transaction.atomic
    def add_document_to_treatment_history(
        self, treatment_history_slug: str = None, document_slug: str = None
    ) -> Document:
        if not self.treatment_history_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                }
            )
        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        if not self.document_repository.is_exist(slug=document_slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        if self.treatment_history_document_repository.is_exist(
            treatment_history_slug=treatment_history_slug,
            document_slug=document_slug,
        ):
            raise exceptions.ValidationError(
                detail={
                    "message": "Конфликт",
                    "description": "Данный документ уже добавлен",
                }
            )
        document = self.document_repository.get(slug=document_slug)
        self.treatment_history_document_repository.create(
            {
                "document": document,
                "treatment_history": treatment_history,
            }
        )
        document_serializer = DocumentSerializer(instance=document)
        return JsonResponse(
            data={
                "document": document_serializer.data,
            }
        )

    @transaction.atomic
    def delete_document_from_treatment_history(
        self, treatment_history_slug: str = None, document_slug: str = None
    ):
        self.treatment_history_document_repository.delete(
            treatment_history_slug=treatment_history_slug,
            document_slug=document_slug,
        )
        return JsonResponse(
            data={
                "treatment_history_slug": treatment_history_slug,
                "deleted_document_slug": document_slug,
            }
        )
