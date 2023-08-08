from flask import render_template
from flask_login import login_required

@login_required
def home():
    return render_template("home.html")
