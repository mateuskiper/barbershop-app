from src.database import db
from src.models.barbers import Barber
from src.models.users import User
from src.services.repository_interface import RepositoryInterface


class BarberRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.__session = db.session

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id):
        return (
            self.__session.query(Barber, User)
            .filter(Barber.id == id)
            .join(User, Barber.user_id == User.id)
            .first()
        )

    def get_services(self, id):
        return self.__session.query(Barber).filter(Barber.id == id).first().services

    def get_by_barbershop(self, barbershop_id):
        return (
            self.__session.query(Barber, User)
            .filter(Barber.barbershop_id == barbershop_id)
            .join(User, Barber.user_id == User.id)
            .all()
        )

    def list(self):
        return self.__session.query(Barber).all()
