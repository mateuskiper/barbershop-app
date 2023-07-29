from flask import Flask
from src import bootstrap, routes, auth


def create_app():
    app = Flask(__name__)

    #auth.init_app(app)
    bootstrap.init_app(app)
    routes.init_app(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
