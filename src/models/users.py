from werkzeug.security import check_password_hash, generate_password_hash

from src.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(140), unique=True)
    username = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(140))
    authenticated = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(40), nullable=True)
    address = db.Column(db.String(140), nullable=True)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def generate_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
