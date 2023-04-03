from rest_framework.authtoken.models import Token


class LogOutService:
    def logout(self, slug: str):
        if Token.objects.filter(user__slug=slug).exists():
            Token.objects.get(user__slug=slug).delete()
