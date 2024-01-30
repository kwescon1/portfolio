from flask import Flask,render_template,request
from services import contact

app = Flask(__name__)

app.config['SECRET_KEY'] ='7aff4eff697d6e2a4d2cff1f529d3d0f'

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
    return render_template('contact.html')

@app.route('/<string:slug>')
def project(slug):
    return render_template('work.html')

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    return contact.submit_form()