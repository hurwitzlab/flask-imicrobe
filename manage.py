#!/usr/bin/env python
import os

from flask_script import Manager, Shell

from app import create_app, db
from app.models import Project


app = create_app(os.environ.get('IMICROBE_FLASK_CONFIG'))
manager = Manager(app)


def make_shell_context():
    # TODO: need all model classes here? should be programmatic
    return {
        'app': app, 'db': db, 'Project': Project
    }


manager.add_command('shell', Shell(make_context=make_shell_context()))


if __name__ == '__main__':
    manager.run()
