from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    UserCode = db.Column(db.String(64), unique=True, index=True)
    Password = db.Column(db.String(128))
    Username = db.Column(db.String(128))
    RoleType = db.Column(db.String(2))

    def __init__(self, UserCode=None, Password=None, Username=None):
        self.UserCode = UserCode
        self.Password = Password
        self.Username = Username

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __repr__(self):
        return '<User %r>' % self.UserName