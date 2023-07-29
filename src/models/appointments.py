import enum

from src.database import db


class AppointmentStatus(enum.Enum):
    scheduled = "scheduled"
    confirmed = "confirmed"
    canceled = "canceled"


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    barbershop_id = db.Column(db.Integer, db.ForeignKey("barbershop.id"))
    barbershop_name = db.Column(db.String(140), db.ForeignKey("barbershop.name"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    service_name = db.Column(db.String(140), db.ForeignKey("service.name"))
    status = db.Column(db.Enum(AppointmentStatus))
