import requests


def test_create_role(book, base_url):
    """Проверка на создание объекта"""
    role_data = {
        "name": "Polonius",
        "type": "Secondary",
        "level": 2,
        "book": book["id"]
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    for key in role_data:
        assert resp_body[key] == role_data[key]


def test_read_role(role, base_url):
    """Проверка на вычитывание объекта"""
    resp = requests.get(f'{base_url}roles/{role["id"]}')
    assert resp.status_code == 200
    resp = resp.json()
    for key in resp:
        assert resp[key] == role[key]


def test_edit_role(role, base_url, book):
    """Проверка на изменение объекта"""
    new_payload = {'name': 'Horace', 'type': 'Main', 'level': 1, 'book': book['id']}
    resp = requests.put(f'{base_url}/roles/{role["id"]}', data=new_payload)
    assert resp.status_code == 200
    resp = resp.json()
    for key in new_payload:
        assert new_payload[key] == resp[key]


def test_delete_role(base_url, book):
    """Проверка на удаление объекта"""
    new_payload = {'name': 'Horace', 'type': 'Main', 'level': 1, 'book': book['id']}
    resp = requests.post(f'{base_url}/roles', data=new_payload)
    delete_r = requests.delete(f'{base_url}/roles/{resp.json()["id"]}')
    assert delete_r.status_code == 204
