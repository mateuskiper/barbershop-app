from src.database import db
from src.models.barbershops import Barbershop
from src.services.repository_interface import RepositoryInterface


class BarbershopRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.__session = db.session

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id):
        return self.__session.query(Barbershop).filter(Barbershop.id == id).first()

    def list(self):
        return self.__session.query(Barbershop).all()
