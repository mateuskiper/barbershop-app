from src.database import db

barber_services_link = db.Table(
    "barber_services_link",
    db.Column("barber_id", db.Integer, db.ForeignKey("barber.id")),
    db.Column("service_id", db.Integer, db.ForeignKey("service.id")),
)


class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(140))
    barbershop_id = db.Column(db.Integer, db.ForeignKey("barbershop.id"))
    services = db.relationship("Service", secondary="barber_services_link")
