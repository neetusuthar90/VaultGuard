from app.main import bp
from flask import Flask,render_template,flash
from flask import request, url_for, redirect
from app.forms.registration import RegistrationForm
from app.forms.login import LoginForm
from flask_login import login_user, current_user
from app.models.user import User
from app import db


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('registration.html',form=form)


@bp.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('main.index'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form = form)

