from src.database import db
from sqlalchemy.types import ARRAY


class Barbershop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    email = db.Column(db.String(140), unique=True)
    phone_number = db.Column(db.String(140), nullable=True)
    address = db.Column(db.String(140), nullable=True)
    barbers = db.Column(ARRAY(db.Integer))
