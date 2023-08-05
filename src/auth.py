from flask_login import LoginManager

def init_app(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    return login_manager