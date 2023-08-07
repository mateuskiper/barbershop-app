from werkzeug.security import check_password_hash, generate_password_hash

from src.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barbershop_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(140), unique=True)
    username = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(140))
    phone_number = db.Column(db.String(40), nullable=True)
    address = db.Column(db.String(140), nullable=True)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
