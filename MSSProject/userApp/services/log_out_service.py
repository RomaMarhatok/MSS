from rest_framework.authtoken.models import Token


class LogOutService:
    def logout(self, user_slug: str) -> None:
        if Token.objects.filter(user__slug=user_slug).exists():
            Token.objects.filter(user__slug=user_slug).first().delete()
