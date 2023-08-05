from flask import Blueprint
from src.controllers.tasks.home import index

tasks = Blueprint("tasks", __name__, template_folder="templates")
tasks.add_url_rule("/", view_func=index)