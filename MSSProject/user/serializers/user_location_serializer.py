from rest_framework.serializers import ModelSerializer, SlugField

from ..models import User, UserLocation


class UserLocationSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")

    class Meta:
        model = UserLocation
        fields = (
            "user_slug",
            "country",
            "city",
            "address",
            "location",
        )

    def create(self, validated_data):
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        instance = UserLocation.objects.create(**validated_data, user=user)
        return instance
