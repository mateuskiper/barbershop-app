from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    # db_user = os.environ["DB_USER"]
    # db_pass = os.environ["DB_PASS"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
