from flask import json

from ..models import Project


class IMicrobeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Project):
            return {'project': {'id': obj.project_id, 'name': obj.project_name}}
        else:
            return json.JSONEncoder.default(obj)
