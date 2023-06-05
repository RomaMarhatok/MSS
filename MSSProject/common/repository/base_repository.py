from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def get(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def list(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def create(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def is_exist(self, **kwargs) -> bool:
        raise NotImplementedError
