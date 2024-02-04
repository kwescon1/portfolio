from flask import render_template,flash,redirect,url_for
from app.services.forms import LoginForm
from app.admin import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template('admin/login.html', form=form)


@bp.route('/')
def index():
    return "logged in"
