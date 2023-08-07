from flask import redirect, url_for
from flask_login import current_user, logout_user

from src.database import db


def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("auth.login"))
