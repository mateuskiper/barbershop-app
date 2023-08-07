from flask import Blueprint
from src.views.auth.login import login
from src.views.auth.logout import logout

auth = Blueprint("auth", __name__, template_folder="templates")
auth.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
auth.add_url_rule("/logout", view_func=logout, methods=["GET"])
