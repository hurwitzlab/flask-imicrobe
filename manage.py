#!/usr/bin/env python
import os

import pytest

from flask_script import Manager

from app import create_app, db


app = create_app(os.environ.get('IMICROBE_FLASK_CONFIG', default='development'))
manager = Manager(app)


@manager.command
def build_tables():
    """Build database tables."""
    db.create_all()


@manager.command
def test():
    """Run unit and functional tests."""
    print('Time for tests')
    pytest.main(['tests'])


if __name__ == '__main__':
    manager.run()
