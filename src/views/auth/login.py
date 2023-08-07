from flask import redirect, render_template, url_for
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

from src.database import db
from src.models.users import User


class LoginForm(FlaskForm):
    email = StringField("E-mail", render_kw={"placeholder": "E-mail"})
    password = PasswordField("Senha", render_kw={"placeholder": "Senha"})
    submit = SubmitField("Entrar", render_kw={"placeholder": "Entrar"})


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.email == form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)

                return redirect(url_for("tasks.home"))

    return render_template("login.html", form=form)
