from flask import abort, render_template
from flask_login import login_required

@login_required
def home():
    products = {}
    return render_template("home.html", products=products)
