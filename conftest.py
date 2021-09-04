import json

import pytest
import requests


@pytest.fixture()
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com/'


@pytest.fixture()
def base_book_url(base_url):
    return base_url + 'books/'


@pytest.fixture()
def base_role_url(base_url):
    return base_url + 'roles/'


@pytest.fixture(scope='session')
def token(base_url):
    r_token = requests.post(f'{base_url}/api-token-auth/',
                            data={'username': 'admin', 'password': 'pass'})
    print(r_token.json())
    return r_token.json()['token']


@pytest.fixture(scope='session')
def headers(token):
    r = {'Content-Type': 'application/json',
         'Authorization': f'Token {token}'}
    return r


books_data = [
    {
        "title": "New Book",
        "author": "Newauthor"
    },
    {
        "title": "@$%^&^&*(()",
        "author": "$^&&*)___)"
    },
    {
        "title": "Новая книга",
        "author": "Новый автор"
    }
]


@pytest.fixture(params=books_data, ids=['latin', "spec symbols", 'cyrrilis'])
def book_data(request):
    res = request.param
    yield res
    # if 'id' in res:
    #     r = requests.delete(f"{base_book_url}{res['id']}")
    #     print(r.url)
    #     print(r.status_code)


@pytest.fixture()
def delete_book(book_data, base_book_url):
    yield
    if 'id' in book_data:
        r = requests.delete(f"{base_book_url}{book_data['id']}")
        print(r.url)
        print(r.status_code)


@pytest.fixture()
def book(base_book_url, book_data, headers):
    data = {
        "title": "For role",
        "author": "For role"
    }
    res = requests.post(base_book_url, headers=headers, data=json.dumps(data))
    yield res.json()
    requests.delete(f"{base_book_url}{res.json()['id']}")


@pytest.fixture()
def role_data(book):
    return {
        "name": "Harry Potter 2",
        "type": "Wizard",
        "level": 1,
        "book": book["id"]
    }


@pytest.fixture
def delete_role():
    pass
