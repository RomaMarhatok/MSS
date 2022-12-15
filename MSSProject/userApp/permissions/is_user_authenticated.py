from rest_framework.permissions import BasePermission
from django.http import HttpRequest
from rest_framework.authtoken.models import Token
from ..models import User


class IsUserAuthenticated(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        print(request.headers)
        if "Authorization" not in request.headers:
            return False
        try:
            key = request.headers["Authorization"].split(" ")[1]
        except IndexError:
            return False
        if not Token.objects.filter(key=key).exists():
            return False
        return True
