import pytest
import requests


@pytest.fixture()
def base_url():
    yield "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture()
def book(base_url):
    book_data = {"title": "Hamlet", "author": "William Shakespeare"}
    resp = requests.post(f'{base_url}/books', data=book_data)
    book_body_resp = resp.json()
    yield book_body_resp
    print(f'{base_url}/books/{book_body_resp["id"]}')
    resp = requests.delete(f'{base_url}/books/{book_body_resp["id"]}')
    assert resp.status_code == 204


@pytest.fixture()
def role(base_url, book):
    role_data = {'name': 'Polonius', 'type': 'Secondary', 'level': '2', 'book': book['id']}
    resp = requests.post(f'{base_url}/roles', data=role_data)
    role_body_resp = resp.json()
    yield role_body_resp
    requests.delete(f'{base_url}/roles/{role_body_resp["id"]}')
