import os

from flask import Flask
from flask_login import LoginManager

from src import bootstrap, database
from src.models.appointments import Appointment
from src.models.barbers import Barber
from src.models.barbershops import Barbershop
from src.models.services import Service
from src.models.users import User
from src.views.auth import auth
from src.views.tasks import tasks


def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config["SECRET_KEY"] = SECRET_KEY

    database.init_app(app)
    bootstrap.init_app(app)

    return app


app = create_app()

# TODO
with app.app_context():
    database.db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return database.db.session.query(User).filter(User.email == user_id).first()


app.register_blueprint(auth)
app.register_blueprint(tasks)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
