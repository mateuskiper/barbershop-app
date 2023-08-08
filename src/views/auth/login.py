from flask import redirect, render_template, url_for
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

from src.services.users_repository import UserRepository

user_repo = UserRepository()


class LoginForm(FlaskForm):
    email = StringField("E-mail", render_kw={"placeholder": "E-mail"})
    password = PasswordField("Senha", render_kw={"placeholder": "Senha"})
    submit = SubmitField("Entrar", render_kw={"placeholder": "Entrar"})


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_repo.get_by_email(form.email.data)
        if user:
            if user.check_password(form.password.data):
                user.authenticated = True
                user_repo.add_to_session(user)
                login_user(user, remember=True)

                return redirect(url_for("tasks.home"))

    return render_template("login.html", form=form)
