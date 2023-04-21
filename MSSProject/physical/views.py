from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet
from common.permissions import IsDoctor, IsUserAuthenticated
from .services.physical_parameters_service import PhysicalParametersSservice


class PhysicalParametersView(GenericViewSet):
    permission_classes = (IsUserAuthenticated,)
    service = PhysicalParametersSservice()

    def retrieve(self, request, slug):
        return self.service.get_physical_parameters(slug)

    def list(self, request, patient_slug: str):
        return self.service.list_physical_parameters(patient_slug)

    class DeleteInputSerializer(serializers.Serializer):
        slug = serializers.SlugField()

    def delete(self, request):
        serializer = self.DeleteInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.delete_physical_parameters(serializer.validated_data)

    class CreateInputSerializer(serializers.Serializer):
        user_slug = serializers.SlugField()
        weight = serializers.FloatField()
        height = serializers.FloatField()
        pressure = serializers.FloatField()

    def create(self, request):
        serializer = self.CreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_physical_parameters(serializer.validated_data)

    class UpdateInputSerializer(serializers.Serializer):
        user_slug = serializers.SlugField()
        slug = serializers.SlugField()
        weight = serializers.FloatField(required=False)
        height = serializers.FloatField(required=False)
        pressure = serializers.FloatField(required=False)

    def update(self, request):
        serializer = self.UpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.update_physical_parameters(serializer.validated_data)
