import json
import requests


def test_positive_book_crete(base_book_url, headers, book_data, delete_book):
    response = requests.post(base_book_url, headers=headers, data=json.dumps(book_data))
    assert response.status_code == 201
    body = response.json()
    assert 'id' in body.keys()
    book_data['id'] = body['id']
    assert body == book_data
