from flask import jsonify

from app.imicrobe import errors

from . import imicrobe
from ..models import Investigator


@imicrobe.route('/investigators/')
def get_investigators():
    investigators = Investigator.query.all()
    return jsonify(investigators)


@imicrobe.route('/investigators/<int:id>')
def get_investigator(id):
    investigator = Investigator.query.get(id)
    if investigator is None:
        return errors.not_found('Investigator with id {} was not found'.format(id))
    return jsonify(investigator)
