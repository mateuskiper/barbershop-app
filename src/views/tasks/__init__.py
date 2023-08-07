from flask import Blueprint
from src.views.tasks.home import home

tasks = Blueprint("tasks", __name__, template_folder="templates")
tasks.add_url_rule("/", view_func=home)