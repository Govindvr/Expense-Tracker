from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment.db'
app.config['SECRET_KEY'] = 'b0abee2e5afa86f079f5d538'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes