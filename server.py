from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from services.forms import ContactForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] ='7aff4eff697d6e2a4d2cff1f529d3d0f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/')
def homepage():
    return render_template('index.html')


project_data = [
    {
        'title': 'Project 1',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work01-hover.jpg'
    },
    {
        'title': 'Project 2',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work02-hover.jpg'
    },
    {
        'title': 'Project 3',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work03-hover.jpg'
    },
    {
        'title': 'Project 4',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work01-hover.jpg'
    },
    {
        'title': 'Project 5',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work02-hover.jpg'
    },
    {
        'title': 'Project 6',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': '/assets/images/work03-hover.jpg'
    },
    {
        'title': 'Project 7',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work01-hover.jpg'
    },
    {
        'title': 'Project 8',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work02-hover.jpg'
    },
    {
        'title': 'Project 9',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work03-hover.jpg'
    },
    {
        'title': 'Project 10',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work01-hover.jpg'
    },
    {
        'title': 'Project 11',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': 'assets/images/work02-hover.jpg'
    },
    {
        'title': 'Project 12',
        'slug': 'this-is-my-dummy-project',
        'description': 'This is a short description for my dummy project',
        'image': '/assets/images/work03-hover.jpg'
    }
]

PER_PAGE = 6

@app.route('/projects')
def projects_page():
    # Group projects into sets of three for the carousel
    grouped_projects = [project_data[i:i+3] for i in range(0, len(project_data), 3)]
    return render_template('works.html', grouped_projects=grouped_projects)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('admin'))
        else:
            flash('Login unsuccessful. Please check username and password','danger')
        
    return render_template('admin/login.html',form=form)

@app.route('/admin')
def admin():
    return "logged in"

@app.route('/<string:slug>')
def project(slug):
    return render_template('work.html')

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    return contact.submit_form()

# if __name__ == 'main':
    # app.run(debug=1)