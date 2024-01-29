from flask import Flask,render_template
from services import contact

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    return contact.submit_form()