from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def list():
        pass
