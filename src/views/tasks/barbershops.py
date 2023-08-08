from flask import abort, render_template, request
from flask_login import login_required

from src.services import barbers_repository, barbershops_repository

barbers_repo = barbers_repository.BarberRepository()
barbershops_repo = barbershops_repository.BarbershopRepository()


@login_required
def barbershops():
    barbershops = barbershops_repo.list() or abort(404, "Nenhuma barbearia encontrada.")

    return render_template("barbershops.html", barbershops=barbershops)


@login_required
def barbers(id: int):
    barbers = barbers_repo.get_by_barbershop(id) or abort(
        404, "Nenhum barbeiro encontrado."
    )

    return render_template("barbers.html", barbers=barbers)


@login_required
def scheduling(id: int, barber_id: int):
    barber = barbers_repo.get(barber_id)
    barber_services = barbers_repo.get_services(barber_id)
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
