import requests
import random
import string


routines_endpoints = {
    'create_routines': 'http://localhost:5000/new-routine',
    'get_routines': 'http://localhost:5000/routines',
    'get_routine': 'http://localhost:5000/get-routine/',
    'login': 'http://localhost:5000/login'
}


def return_post_endpoint(endpoint, body=None, token='', params = ''):
    response = requests.post(
        routines_endpoints[endpoint] + params, 
        json=body,
        headers={
            'Authorization': token
        }
    )
    return response

def return_get_endpoint(endpoint, token='', params = ''):
    response = requests.get(
        routines_endpoints[endpoint] + params, 
        headers={
            'Authorization': token
        }
    )
    return response

res = return_post_endpoint('login', { "username": "angel", "password": "angel" })
json = res.json()
print(res, json)
token = json['token']

def test_create_routine():
    res = return_post_endpoint('create_routines', '', token=token)
    assert res.status_code == 400

    res = return_post_endpoint('create_routines', '')
    assert res.status_code == 401

    res = return_post_endpoint('create_routines', { 'name': 'jejeje' }, token=token)
    assert res.status_code == 400

    res = return_post_endpoint('create_routines', { 'name': 'routine', 'label': 'no-label ' }, token=token)
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

def test_get_routines():
    res = return_get_endpoint('get_routines', token=None)
    assert res.status_code == 401

    res = return_get_endpoint('get_routines', token=token)
    assert res.status_code == 200
    json = res.json()
    assert json['success'] == True

def test_get_routine():
    res = return_get_endpoint('get_routine', token=None, params='routine')
    assert res.status_code == 401

    res = return_get_endpoint('get_routine', token=token, params='no-routine-jeje')
    assert res.status_code == 400

    res = return_get_endpoint('get_routine', token=token, params='routine')
    assert res.status_code == 200
    json = res.json()
    assert json['success'] == True

