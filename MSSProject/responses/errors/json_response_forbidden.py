from rest_framework import status
from django.http import JsonResponse


class JsonResponseForbidden(JsonResponse):
    status_code = status.HTTP_403_FORBIDDEN
