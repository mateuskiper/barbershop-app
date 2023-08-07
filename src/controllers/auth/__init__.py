from flask import Blueprint
from src.controllers.auth.login import login, logout

auth = Blueprint("auth", __name__, template_folder="templates")
auth.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
auth.add_url_rule("/logout", view_func=logout, methods=["GET", "POST"])
