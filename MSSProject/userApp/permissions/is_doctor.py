from django.http import HttpRequest
from ..models.role import Role
from ..models.user import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAcceptable
from rest_framework import status


class IsDoctor(BasePermission):
    message = "Access denied for not doctor user"

    def has_permission(self, request: HttpRequest, view) -> bool:
        if "Authorization" not in request.headers:
            return False
        try:
            key = request.headers["Authorization"].split(" ")[1]
        except IndexError:
            return False
        if not Token.objects.filter(key=key).exists():
            return False
        token = Token.objects.select_related("user", "user__role").get(key=key)
        if token.user.role.name == Role.DOCTOR:
            return True
        raise NotAcceptable(detail=self.message)
