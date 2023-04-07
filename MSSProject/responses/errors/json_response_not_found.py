from django.http import JsonResponse


class JsonResponseNotFound(JsonResponse):
    status_code = 404
