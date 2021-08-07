import json
import requests


def test_positive_role_crete(base_role_url, headers, role_data, delete_role):
    response = requests.post(base_role_url, headers=headers, data=json.dumps(role_data))
    assert response.status_code == 201
