from rest_framework import status
from django.http import JsonResponse


class JsonResponseRecordExist(JsonResponse):
    status_code = status.HTTP_302_FOUND
