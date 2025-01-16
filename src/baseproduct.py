from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """базовый абстрактный класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
