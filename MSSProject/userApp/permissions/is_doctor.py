from django.http import HttpRequest
from ..models.role import Role
from ..models.user import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        if "Authorization" not in request.headers:
            return False
        try:
            key = request.headers["Authorization"].split(" ")[1]
        except IndexError:
            return False
        if not Token.objects.filter(key=key).exists():
            return False
        token: User = Token.objects.filter(key=key).first().user
        if token.role.name == "doctor":
            return True
        return False
