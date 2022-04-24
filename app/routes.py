from app import app
from flask import render_template, request, redirect, url_for, flash
from app.database import User,Investment
from app.forms import RegisterForm,LoginForm
from app import db

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        print(form.username.data)
    return render_template("login.html",form=form)
    

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,name = form.name.data,
                                email = form.email.data, Password = form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg,category='danger')
    return render_template('register.html',form = form)
