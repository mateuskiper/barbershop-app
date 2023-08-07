from flask import abort, render_template, request
from flask_login import login_required

from src.database import db
from src.models.barbershops import Barbershop
from src.models.barbers import Barber


@login_required
def barbershops():
    barbershops = db.session.query(Barbershop).all() or abort(
        404, "Nenhuma barbearia encontrada."
    )

    return render_template("barbershops.html", barbershops=barbershops)


@login_required
def barbers(id: int):
    barbers = db.session.query(Barber).filter(
        Barber.barbershop_id == id
    ).all() or abort(404, "Nenhuma barbearia encontrada.")

    return render_template("barbers.html", barbers=barbers)


@login_required
def scheduling(id: int, barber_id: int):
    return render_template("scheduling.html")


@login_required
def scheduled():
    datetime = request.form["datetime"]
    return "Agendamento efetuado para " + datetime
