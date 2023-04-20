from django.db import transaction
from django.http import JsonResponse
from rest_framework import exceptions
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin
from ..repositories.physical_parameters_repository import PhysicalParametersRepository
from ..serializers import PhysicalParametersSerializer


class PhysicalParametersSservice(IsUserExistMixin):
    def __init__(self) -> None:
        self.physical_parameters_repository = PhysicalParametersRepository()

    def get_physical_parameters(self, slug):
        if not self.physical_parameters_repository.is_exist(slug=slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не найдено",
                    "description": "Физические параметры с таким slug не найдены",
                }
            )
        ps_instance = self.physical_parameters_repository.get(slug=slug)
        serializer = PhysicalParametersSerializer(instance=ps_instance)
        return JsonResponse(data={"physical_parameter": serializer.data})

    def list_physical_parameters(self, patient_slug: str):
        if self.is_user_exist(patient_slug):
            physical_parameters = self.physical_parameters_repository.list(
                patient_slug=patient_slug
            )
        serializerd_ps = PhysicalParametersSerializer(
            instance=physical_parameters, many=True
        ).data
        return JsonResponse(
            {
                "physical_parameters": serializerd_ps,
            }
        )

    @transaction.atomic
    def create_physical_parameters(self, data: dict):
        user_slug = data.get("user_slug", None)
        self.is_user_exist(user_slug)
        ph = self.physical_parameters_repository.create(data)
        serializer = PhysicalParametersSerializer(instance=ph)
        return JsonResponse(data={"physical_parameters": serializer.data})

    @transaction.atomic
    def delete_physical_parameters(self, data: dict):
        slug = data.get("slug", None)
        if not self.physical_parameters_repository.is_exist(slug=slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не найдено",
                    "description": "Физические параметры с таким slug не найдены",
                }
            )
        self.physical_parameters_repository.delete(slug=slug)
        return JsonResponse(data={"physical_parameters_deleted_slug": slug})

    @transaction.atomic
    def update_physical_parameters(self, data):
        patient_slug = data.get("user_slug", None)
        self.is_user_exist(patient_slug)
        slug = data.get("slug", None)
        if not self.physical_parameters_repository.is_exist(slug=slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не найдено",
                    "description": "Физические параметры с таким slug не найдены",
                }
            )
        physical_parameters_before_update = self.physical_parameters_repository.get(
            slug=slug
        )
        physical_parameters = self.physical_parameters_repository.update(
            data, physical_parameters_before_update
        )
        serializer = PhysicalParametersSerializer(instance=physical_parameters)
        return JsonResponse(data={"physical_parameter": serializer.data})
