import pytest
import requests
import json
import csv


def test_get(base_url):
    r = requests.get(base_url)
    print(base_url)
    assert r.status_code == 200


def test_create_book(base_url, book):
    pass


with open('test_data.csv', encoding='utf-8') as csvfile:
    books = []
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        book = {row[0]: row[1], row[2]: row[3]}
        books.append(book)
print(books)


@pytest.mark.parametrize("book_list", books)
def test_book_create_n(base_url, book_list, book):
    b = requests.post(f"{base_url}/books", data=book_list)
    assert b.status_code == 201
    book.update(b.json())


with open('role_data.json', 'r', encoding='utf-8') as f:
    role_data = json.load(f)
print(role_data)


@pytest.mark.parametrize("role_list", role_data)
def test_create_role(book_create, base_url, role_list):
    role_list.update({"book": book_create["id"]})
    print(role_list)
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    for key in role_list:
        assert resp_body[key] == role_list[key]


def test_create_role(book, base_url):
    role_data = {
        "name": "Polonius",
        "type": "Secondary",
        "level": 26,
        "book": 15
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 400

