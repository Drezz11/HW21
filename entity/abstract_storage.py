from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def __add__(self, name: str, amount: int) -> None:
        pass


    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass


    @abstractmethod
    def get_items(self):
        pass


    @abstractmethod
    def get_unique_items_count(self):
        pass