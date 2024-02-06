from flask import render_template,flash,redirect,url_for,request
from app.webforms.forms import LoginForm
from app.auth import bp
from app.extensions import bcrypt
from flask_login import login_user,current_user,logout_user,login_required
from app.models.user import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # redirect user if already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = LoginForm()

    if form.validate_on_submit():

        # check user exists
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            # redirect to next page if exists
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('admin.index'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')

    return render_template('admin/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))