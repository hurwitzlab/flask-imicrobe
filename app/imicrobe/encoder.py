from flask import json

from app import db


class IMicrobeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, db.Model):
            return obj.json()
        else:
            return json.JSONEncoder.default(obj)
