from rest_framework.views import APIView
from ..models import User
from django.http import JsonResponse, HttpRequest
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status


class AuthenticationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        if "login" not in request.data or "password" not in request.data:
            return JsonResponse(
                data={"errors": ["login or password don't provided"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login = request.data["login"]
        password = request.data["password"]
        if User.is_exist(login, password):
            user = User.get_user_by_login(login)
            user_auth_token_key = Token.objects.filter(user=user).first().key
            return JsonResponse(
                data={
                    "message": "user successful authenticated",
                    "token": user_auth_token_key,
                    "user_role": user.role.name,
                },
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            data={"errors": ["user don't exist"]}, status=status.HTTP_400_BAD_REQUEST
        )
