from src.database import db
from sqlalchemy.types import ARRAY


class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140))
    services = db.Column(ARRAY(db.Integer))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    barbershop_id = db.Column(db.Integer, db.ForeignKey("barbershop.id"))
