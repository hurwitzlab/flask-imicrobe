from flask import jsonify

from app.imicrobe import errors

from . import imicrobe
from ..models import Project


@imicrobe.route('/projects/')
def get_projects():
    projects = Project.query.all()
    return jsonify(projects)


@imicrobe.route('/projects/<int:id>')
def get_project(id):
    project = Project.query.get(id)
    if project is None:
        return errors.not_found('Project with id {} was not found'.format(id))
    return jsonify(project)
