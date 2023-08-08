from src.database import db
from sqlalchemy.types import ARRAY


class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(140))
    barbershop_id = db.Column(db.Integer, db.ForeignKey("barbershop.id"))
    services = db.Column(ARRAY(db.Integer))
