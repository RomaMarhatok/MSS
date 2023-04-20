from django.http import JsonResponse
from rest_framework import status


class JsonResponseNotFound(JsonResponse):
    status_code = status.HTTP_404_NOT_FOUND
