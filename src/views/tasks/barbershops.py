from flask import abort, render_template, request
from flask_login import login_required

from src.services import barbers_repository, barbershops_repository, services_repository

barbers_repo = barbers_repository.BarberRepository()
barbershops_repo = barbershops_repository.BarbershopRepository()
services_repo = services_repository.ServiceRepository()


@login_required
def barbershops():
    barbershops = barbershops_repo.list() or abort(404, "Nenhuma barbearia encontrada.")

    return render_template("barbershops.html", barbershops=barbershops)


@login_required
def barbers(id: int):
    barbers_raw = barbers_repo.get_by_barbershop(id) or abort(
        404, "Nenhum barbeiro encontrado."
    )

    barbers = []
    for b in barbers_raw:
        barber = b[0]
        barber.name = b[1].name
        barbers.append(barber)

        del barber

    return render_template("barbers.html", barbers=barbers)


@login_required
def scheduling(id: int, barber_id: int):
    barber_raw = barbers_repo.get(barber_id)
    barber = barber_raw[0]
    barber.name = barber_raw[1].name
    barber_services = services_repo.get(barber.services)
    barbershop = barbershops_repo.get(id)

    return render_template(
        "scheduling.html",
        barber=barber,
        barbershop=barbershop,
        services=barber_services,
    )


@login_required
def scheduled():
    schedule_datetime = request.form["schedule_datetime"]
    return render_template("scheduled.html", schedule_datetime=schedule_datetime)
