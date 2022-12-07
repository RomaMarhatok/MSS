from __future__ import annotations
from rest_framework.serializers import ModelSerializer


class SerializerService:
    def __init__(self, class_serializer: ModelSerializer, data) -> None:
        self.class_serializer = class_serializer
        self.data = data
        self.errors = None
        self.serialize_instance = None
        self.__serialize()

    def __serialize(self) -> SerializerService:
        serializer = self.class_serializer(data=self.data)
        if not serializer.is_valid():
            self.errors = serializer.errors
        self.serialize_instance = serializer.save()
        return self
