from flask import render_template,flash,redirect,url_for
from app.services.forms import LoginForm
from app.auth import bp
from app.extensions import bcrypt
from flask_login import login_user
from app.models.user import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # check user exists
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('admin.index'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')

    return render_template('admin/login.html', form=form)


@bp.route('/logout')
def logout():
    return "logged out"