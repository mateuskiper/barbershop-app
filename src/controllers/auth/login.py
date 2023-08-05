from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from werkzeug.urls import url_parse
from wtforms import PasswordField, StringField, SubmitField

from src.models.users import User


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Submit")

def login():
    nologin = False
    if current_user.is_authenticated:
        return redirect(url_for("tasks.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            nologin = True
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("tasks.index")
            return redirect(next_page)
    return render_template(
        "login.html", title="Sign In", form=form, message=nologin
    )

def logout():
    logout_user()
    return redirect(url_for("index"))
