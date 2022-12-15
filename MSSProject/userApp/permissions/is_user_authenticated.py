from rest_framework.permissions import BasePermission
from django.http import HttpRequest
from rest_framework.authtoken.models import Token
from ..models import User


class IsUserAuthenticated(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        if "Authorization" not in request.headers:
            return False
        key = request.headers["Authorization"].split(" ")[1]
        if not Token.objects.filter(key=key).exists():
            return False
        return True
