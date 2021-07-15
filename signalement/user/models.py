from sqlalchemy import Column, desc
from sqlalchemy.orm import backref

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from signalement.extensions import db
from signalement.utils import get_current_time
from signalement.constants import *

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255), nullable=False, unique=True)
    email = Column(db.String(255), nullable=False, unique=True)
    phone = Column(db.String(255), nullable=True, default="")
    created_at = Column(db.DateTime, nullable=False, default=get_current_time)

    _password = Column('password', db.String(200), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = db.synonym('_password', descriptor=property(_get_password, _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    role_code = Column(db.SmallInteger, default=MODO, nullable=False)

    @property
    def role(self):
        return USER_ROLE[self.role_code]

    def is_admin(self):
        return self.role_code == ADMIN

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(db.or_(
            USer.name == login, User.email == login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first_or_404()
