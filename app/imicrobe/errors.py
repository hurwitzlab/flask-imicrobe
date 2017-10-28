from flask import jsonify

from . import imicrobe


@imicrobe.app_errorhandler(403)
def forbidden(message):
    ##response = jsonify({'error': 'forbidden', 'message': message})
    response = jsonify({'error': 'forbidden'})
    response.status_code = 403
    return response


@imicrobe.app_errorhandler(404)
def not_found(message):
    ##response = jsonify({'error': 'Not found', 'message': message})
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response
