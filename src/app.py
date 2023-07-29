from flask import Flask
from src import bootstrap, routes, database
from src.models.appointments import Appointment
from src.models.barbershops import Barbershop
from src.models.services import Service
from src.models.users import User


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    bootstrap.init_app(app)
    routes.init_app(app)

    return app


app = create_app()

# TODO
with app.app_context():
    database.db.create_all()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
