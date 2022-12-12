from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from ..serializers.user_serializer import UserDocumentSerializer
from ..models import UserDocument
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from rest_framework.authtoken.models import Token
from ..services.serializer_service import SerializerService


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest):
        if "Authorization" in request.headers:
            key = request.headers["Authorization"].split(" ")[1]
            try:
                user = Token.objects.get(key=key).user
            except Token.DoesNotExist:
                return JsonResponse(
                    data={"errors": ["authentication token doesn't exist"]}
                )
            user_docuements = UserDocument.objects.filter(user=user)
            serializer = UserDocumentSerializer(user_docuements, many=True)
            if serializer.is_valid():
                return JsonResponse(
                    data={"user_documents": serializer.data}, status=status.HTTP_200_OK
                )
        return JsonResponse(
            data={"errors": ["authentication token doesn't provided"]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def create(self, request):
        serializer_service = SerializerService(UserDocumentSerializer, request.data)
        if serializer_service.errors is not None:
            return JsonResponse(
                data={"errors": serializer_service.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return JsonResponse(data={}, status=status.HTTP_200_OK)

    def retrieve(self, request, slug=None):
        user_document = UserDocument.objects.filter(slug=slug).first()
        serializer = UserDocumentSerializer(instance=user_document)
        return JsonResponse(
            data={"user_document": serializer.data}, status=status.HTTP_200_OK
        )
