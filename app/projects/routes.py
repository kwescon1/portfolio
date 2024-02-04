from flask import render_template
from app.projects import bp


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

@bp.route('/')
def index():
    # Group projects into sets of three for the carousel
    grouped_projects = [project_data[i:i+3] for i in range(0, len(project_data), 3)]
    return render_template('works.html', grouped_projects=grouped_projects)

@bp.route('/<string:slug>')
def project(slug):
    return render_template('work.html')