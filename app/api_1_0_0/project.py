from flask import jsonify

from . import api
from ..models import Project


@api.route('/project/')
def get_projects():
    projects = Project.query.all()
    return jsonify([project for project in projects])

@api.route('/project/<int:id>')
def get_project(id):
    project = Project.query.get(id)
    return jsonify(project)
