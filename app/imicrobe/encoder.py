from flask import json

from ..models import Project


class IMicrobeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Project):
            return {'project': {'project_id': obj.project_id, 'project_name': obj.project_name}}
        else:
            return json.JSONEncoder.default(obj)
