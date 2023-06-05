from django.db import transaction
from rest_framework.authtoken.models import Token


class LogOutService:
    @transaction.atomic
    def logout(self, slug: str):
        if Token.objects.filter(user__slug=slug).exists():
            Token.objects.get(user__slug=slug).delete()
