from src.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    barbershop_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(140))
    email = db.Column(db.String(140), unique=True)
    username = db.Column(db.String(140), unique=True)
    password = db.Column(db.String(512))
    phone_number = db.Column(db.String(140), nullable=True)
    address = db.Column(db.String(140), nullable=True)
