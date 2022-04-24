from app import db
from app import bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30),nullable=False)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password = db.Column(db.String(length=60), nullable= False)
    investment = db.relationship('Investment',backref='owned_user',lazy = True)

    @property
    def Password(self):
        return self.Password

    @Password.setter
    def Password(self,plain_text):
        self.password = bcrypt.generate_password_hash(plain_text).decode('utf-8')

class Investment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Integer())
    typeOfInvestment = db.Column(db.String(length=10))
    date = db.Column(db.Date())
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

