import enum

from sqlalchemy.types import ARRAY

from src.database import db


class AppointmentStatus(enum.Enum):
    scheduled = "scheduled"
    confirmed = "confirmed"
    canceled = "canceled"


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    barber_id = db.Column(db.Integer, db.ForeignKey("barber.id"))
    barber_name = db.Column(db.String(140), db.ForeignKey("barber.name"))
    services = db.Column(ARRAY(db.Integer))
    status = db.Column(db.Enum(AppointmentStatus))
