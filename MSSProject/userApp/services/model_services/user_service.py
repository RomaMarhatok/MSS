from ...models import User, UserPersonalInfo
from ...serializers.user_serializer import UserPersonalInfoSerializer, UserSerializer
from django.db.models import Q
from rest_framework.authtoken.models import Token


class UserService:
    def get_user_personal_info(self, slug) -> dict:
        user = User.objects.filter(slug=slug).first()
        user_personal_info = UserPersonalInfo.objects.filter(user=user).first()
        serializer = UserPersonalInfoSerializer(instance=user_personal_info)
        return serializer.data

    def is_user_exist(self, login, password) -> bool:
        return User.objects.filter(Q(login=login) & Q(password=password)).exists()

    def get_user_by_token(self, token_key: str) -> User:
        return Token.objects.filter(key=token_key).first().user

    def get_user_by_login(self, login: str) -> User:
        return User.objects.filter(login=login).first()

    def get_user_by_slug(self, slug):
        return User.objects.filter(slug=slug).first()

    def serialize_user_model(self, user: User) -> dict:
        serializer = UserSerializer(instance=user)
        return serializer.data
