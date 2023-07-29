from src.database import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    barbershop_id = db.Column(db.Integer)
    description = db.Column(db.String(140), nullable=True)
