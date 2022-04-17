from flask_login import UserMixin
from datetime import datetime
from . import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique = True, index = True)
  password_hash = db.Column(db.String(150))
  time = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  

  def check_password(self,password):
        return check_password_hash(self.password_hash,password)