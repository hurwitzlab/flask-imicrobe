"""
These functions expect to find a server running at localhost:5000.
"""
import pytest
import requests

from app import db

from app.models import Investigator


rest_url = 'http://localhost:5000'

@pytest.fixture
def app_server_db():
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()


def test_investigators__0(app_server_db):

    r = requests.get(url=rest_url + '/investigators/')
    assert r.status_code == 200
    r_investigators = r.json()
    assert len(r_investigators) == 0

    r = requests.get(url= rest_url + '/investigators/1')
    assert r.status_code == 404
    r_error = r.json()
    assert 'error' in r_error
    assert 'message' in r_error


def test_investigators__1(app_server_db):

    investigator_1 = Investigator(investigator_name='investigator_1')
    app_server_db.session.add(investigator_1)
    app_server_db.session.commit()

    r = requests.get(url=rest_url + '/investigators/1')
    assert r.status_code == 200
    r_investigator = r.json()
    print(r_investigator)
    assert r_investigator['investigator_name'] == investigator_1.investigator_name

    r = requests.get(url=rest_url + '/investigators/')
    assert r.status_code == 200
    r_investigators = r.json()
    assert len(r_investigators) == 1
    assert r_investigators[0]['investigator_name'] == investigator_1.investigator_name


def test_investigators__2(app_server_db):

    investigator_1 = Investigator(investigator_name='investigator_1')
    app_server_db.session.add(investigator_1)
    app_server_db.session.commit()

    investigator_2 = Investigator(investigator_name='investigator_2')
    app_server_db.session.add(investigator_2)
    app_server_db.session.commit()

    r = requests.get(url=rest_url + '/investigators/1')
    assert r.status_code == 200
    r_investigator = r.json()
    print(r_investigator)
    assert r_investigator['investigator_name'] == investigator_1.investigator_name

    r = requests.get(url=rest_url + '/investigators/2')
    assert r.status_code == 200
    r_investigator = r.json()
    print(r_investigator)
    assert r_investigator['investigator_name'] == investigator_2.investigator_name

    # will the results always be in sorted order according to investigator_id?
    r = requests.get(url=rest_url + '/investigators/')
    assert r.status_code == 200
    r_investigators = r.json()
    print(r_investigators)
    assert len(r_investigators) == 2
    assert r_investigators[0]['investigator_name'] == investigator_1.investigator_name
    assert r_investigators[1]['investigator_name'] == investigator_2.investigator_name
