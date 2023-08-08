from src.database import db
from src.models.services import Service
from src.services.repository_interface import RepositoryInterface


class ServiceRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.__session = db.session

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id_list):
        return self.__session.query(Service).filter(Service.id.in_(id_list)).all()

    def list(self):
        return self.__session.query(Service).all()
