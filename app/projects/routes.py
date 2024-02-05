from flask import render_template
from app.projects import bp
from app.extensions import db
from  app.models.project import Project


PER_PAGE = 6

@bp.route('/')
def index():
    project_data = Project.query.all()
    # Group projects into sets of three for the carousel
    grouped_projects = [project_data[i:i+3] for i in range(0, len(project_data), 3)]
    return render_template('works.html', grouped_projects=grouped_projects)

@bp.route('/<string:slug>')
def project(slug):
    return render_template('work.html')