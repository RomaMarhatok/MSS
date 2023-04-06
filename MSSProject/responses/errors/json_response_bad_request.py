from rest_framework import status
from django.http import JsonResponse


class JsonResponseBadRequest(JsonResponse):
    status_code = status.HTTP_400_BAD_REQUEST
