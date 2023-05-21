import requests
import random
import string


routines_endpoints = {
    'create_routines': 'http://localhost:5000/new-routine',
    'login': 'http://localhost:5000/login'
}


def return_endpoint(endpoint, body=None, token=''):
    response = requests.post(
        routines_endpoints[endpoint], 
        json=body,
        headers={
            'Authorization': token
        }
    )
    return response

res = return_endpoint('login', { "username": "angel", "password": "angel" })
json = res.json()
token = json['token']

def test_create_routine():
    res = return_endpoint('create_routines', '', token=token)
    assert res.status_code == 400

    res = return_endpoint('create_routines', '')
    assert res.status_code == 401

    res = return_endpoint('create_routines', { 'name': 'jejeje' }, token=token)
    assert res.status_code == 400

    res = return_endpoint('create_routines', { 'name': 'routine', 'label': 'no-label ' }, token=token)
    assert res.status_code == 400

    """
    # I comment this for not create infinite routines
    name = ''.join(random.choices(string.ascii_uppercase, k=8))
    label = ''.join(random.choices(string.ascii_uppercase, k=8))

    res = return_endpoint('create_routines', { 'name': name, 'label': label }, token=token)
    assert res.status_code == 200

    json = res.json()
    assert json['success'] == True
    """

