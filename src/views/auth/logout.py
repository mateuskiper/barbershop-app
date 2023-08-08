from flask import redirect, url_for
from flask_login import current_user, logout_user

from src.services.users_repository import UserRepository

user_repo = UserRepository()


def logout():
    user = current_user
    user.authenticated = False
    user_repo.add_to_session(user)
    logout_user()
    return redirect(url_for("auth.login"))
