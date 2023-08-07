from flask import Blueprint
from src.views.tasks.home import home
from src.views.tasks.barbershops import barbershops, barbers, scheduling, scheduled

tasks = Blueprint("tasks", __name__, template_folder="templates")
tasks.add_url_rule("/", view_func=home)
tasks.add_url_rule("/barbershops", view_func=barbershops)
tasks.add_url_rule("/barbershops/<int:id>", view_func=barbers)
tasks.add_url_rule("/barbershops/<int:id>/<int:barber_id>", view_func=scheduling)
tasks.add_url_rule("/scheduled", view_func=scheduled, methods=["GET", "POST"])
