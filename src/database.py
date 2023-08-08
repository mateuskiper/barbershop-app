import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_host = os.environ["DB_HOST"]
    db_name = os.environ["DB_NAME"]

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
    db.init_app(app)
