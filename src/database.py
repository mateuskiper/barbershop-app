import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()


def init_app(app):
    db_user = os.environ["RDS_USERNAME"]
    db_pass = os.environ["RDS_PASSWORD"]
    db_host = os.environ["RDS_HOSTNAME"]
    db_name = os.environ["RDS_DB_NAME"]

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
    db.init_app(app)
