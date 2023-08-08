from src.database import db
from src.models.users import User
from src.services.repository_interface import RepositoryInterface


class UserRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.__session = db.session

    def create(self):
        pass

    def add_to_session(self, user):
        self.__session.add(user)
        self.__session.commit()

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id):
        return self.__session.query(User).filter(User.id == id).first()

    def get_by_email(self, email):
        return self.__session.query(User).filter(User.email == email).first()

    def list(self):
        return self.__session.query(User).all()
