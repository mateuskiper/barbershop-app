from flask import abort, render_template
from flask_login import login_required

@login_required
def index():
    products = {}
    return render_template("index.html", products=products)
