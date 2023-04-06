from django.http import JsonResponse


class JsonResponseValidationErrors(JsonResponse):
    status_code = 400
