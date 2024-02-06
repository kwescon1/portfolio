from flask import render_template
from app.webforms.forms import ContactForm
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html',form=form)