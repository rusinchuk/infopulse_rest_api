import requests

### Basic Authentication request:
r = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                  data={'title': 'Anna Karenina', 'author': '111'},
                  auth=('admin', 'pass'))
print(r.status_code)
print(r.headers)
print(r.text)


### Using Session
session = requests.Session()
session.auth = ('admin', 'pass')

r1 = session.get('http://pulse-rest-testing.herokuapp.com/roles2?level=100500')
print(r1.status_code)
print(r1.headers)
print(r1.text)


### Token Authentication:
# Запрос на получение токена (можно сделать один раз и потом им пользоваться.
# Так на практике чаще делают: запращивают токен и потом им пользуются вместо передачи user и password)
r_token = requests.post('http://pulse-rest-testing.herokuapp.com/api-token-auth/',
                        data={'username': 'admin', 'password': 'pass'})

print(r_token.status_code)
print(r_token.text)
print(r_token.json())
token = r_token.json()['token']
print(token)

# Token Authentication request:
r2 = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                   # params={"token": token},
                   data={'title': 'Anna Karenina', 'author': '111'},
                   headers={'Authorization': f'Token {token}'})

print(r2.url)
print(r2.status_code)
print(r2.text)


### Token Authentication with Session:
print(session.headers)
session.headers.update({'Authorization': f'Token {token}'})
print(session.headers)

r3 = session.get('http://pulse-rest-testing.herokuapp.com/roles2')
print(r3.status_code)
print(r3.text)
