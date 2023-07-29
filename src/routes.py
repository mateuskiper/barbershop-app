from flask import Blueprint

from src.controllers.home import index, login

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/login", view_func=login)
# bp.add_url_rule(
#     "/product/<product_id>", view_func=product, endpoint="productview"
# )


def init_app(app):
    app.register_blueprint(bp)