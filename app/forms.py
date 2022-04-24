from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.database import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('User already exist')
    
    def validate_email(self, email_to_check):
        user_email = User.query.filter_by(email=email_to_check.data).first()
        if user_email:
            raise ValidationError('Email already exist')


    username = StringField(label="Username",validators=[Length(min=2, max= 30), DataRequired()])
    name = StringField(label="Name",validators=[Length(min=2, max= 30), DataRequired()])
    email = StringField(label="Email",validators=[Length(min=8, max= 50),Email(), DataRequired()])
    password = PasswordField(label = "Password",validators=[Length(min=4), DataRequired()])
    confirm = PasswordField(label= "Confirm",validators= [EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label="Username")
    password = PasswordField(label = "Password")
    submit = SubmitField(label='Submit')