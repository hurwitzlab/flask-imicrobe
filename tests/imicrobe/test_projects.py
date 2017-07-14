"""
These functions expect to find a server running at localhost:5000.
"""
import pytest
import requests

from app import db

from app.models import Project


@pytest.fixture
def app_server_db():
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()


def test_projects__0(app_server_db):

    r = requests.get(url='http://localhost:5000/imicrobe/projects/')
    assert r.status_code == 200
    r_projects = r.json()
    assert len(r_projects) == 0

    r = requests.get(url='http://localhost:5000/imicrobe/projects/1')
    assert r.status_code == 404
    r_error = r.json()
    assert 'error' in r_error
    assert 'message' in r_error


def test_projects__1(app_server_db):

    project_1 = Project(project_name='project_1')
    app_server_db.session.add(project_1)
    app_server_db.session.commit()

    r = requests.get(url='http://localhost:5000/imicrobe/projects/1')
    assert r.status_code == 200
    r_project = r.json()
    print(r_project)
    assert r_project['project']['project_name'] == project_1.project_name

    r = requests.get(url='http://localhost:5000/imicrobe/projects/')
    assert r.status_code == 200
    r_projects = r.json()
    assert len(r_projects) == 1
    assert r_projects[0]['project']['project_name'] == project_1.project_name


def test_projects__2(app_server_db):

    project_1 = Project(project_name='project_1')
    app_server_db.session.add(project_1)
    app_server_db.session.commit()

    project_2 = Project(project_name='project_2')
    app_server_db.session.add(project_2)
    app_server_db.session.commit()

    r = requests.get(url='http://localhost:5000/imicrobe/projects/1')
    assert r.status_code == 200
    r_project = r.json()
    print(r_project)
    assert r_project['project']['project_name'] == project_1.project_name

    r = requests.get(url='http://localhost:5000/imicrobe/projects/2')
    assert r.status_code == 200
    r_project = r.json()
    print(r_project)
    assert r_project['project']['project_name'] == project_2.project_name

    # will the results always be in sorted order according to project_id?
    r = requests.get(url='http://localhost:5000/imicrobe/projects/')
    assert r.status_code == 200
    r_projects = r.json()
    print(r_projects)
    assert len(r_projects) == 2
    assert r_projects[0]['project']['project_name'] == project_1.project_name
    assert r_projects[1]['project']['project_name'] == project_2.project_name
