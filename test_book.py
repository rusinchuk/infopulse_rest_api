import requests


def test_create_book(base_url, book):
    """Проверка на создание объекта"""
    payload = {'title': 'Hamlet', 'author': 'William Shakespeare'}
    resp = requests.post(f'{base_url}/books', data=payload)
    assert 'id' in resp.json()
    for key in payload:
        assert payload[key] == resp.json()[key]


def test_read_book(base_url, book):
    """Проверка на вычитывание объекта"""
    assert requests.get(f'{base_url}/books/{book["id"]}').status_code == 200


def test_edit_book(base_url, book):
    """Проверка на изменение объекта"""
    new_payload = {'title': 'Dombey and Son', 'author': 'Charles Dickens'}
    old_book = requests.get(f'{base_url}/books/{book["id"]}')
    change_r = requests.put(f'{base_url}/books/{book["id"]}', data=new_payload)
    for key in new_payload:
        assert old_book.json()[key] != new_payload[key]

    for key in new_payload:
        assert new_payload[key] == change_r.json()[key]


def test_delete_book(base_url, book):
    """Проверка на удаление объекта"""
    payload = {'title': 'Son', 'author': 'Jack'}
    resp = requests.post(f'{base_url}/books', data=payload)
    delete_b = requests.delete(f'{base_url}/books/{resp.json()["id"]}')
    assert delete_b.status_code == 204

