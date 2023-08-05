from flask import Blueprint
from src.controllers.auth.login import login

auth = Blueprint("auth", __name__, template_folder="templates")
auth.add_url_rule("/login", view_func=login)