import requests
import random
import string


auth_endpoints = {
    'register': 'http://localhost:5000/register',
    'login': 'http://localhost:5000/login'
}

def return_endpoint(endpoint, body=None):
    response = requests.post(
        auth_endpoints[endpoint], 
        json=body               
    )
    return response

def test_register():
    res = return_endpoint('register', '')
    assert res.status_code == 400
    res = return_endpoint('register', { "username": "angel" })
    assert res.status_code == 400
    res = return_endpoint('register', { "username": 'angel', 'password': '', 'email': 'angel', 'repeat_password': 'angel' })
    assert res.status_code == 401
    
    username = ''.join(random.choices(string.ascii_uppercase, k=8))
    email = ''.join(random.choices(string.ascii_uppercase, k=8))
    pasword = ''.join(random.choices(string.ascii_uppercase, k=8))
    repeat_password = ''.join(random.choices(string.ascii_uppercase, k=8))

    """
    Run only if this user exits
    res = return_endpoint('register', { "username": username, 'password': pasword, 'email': email, 'repeat_password': repeat_password })
    assert res.status_code ==  401
    """

    """
    # I comment this for not create infinite users
    repeat_password = pasword
    res = return_endpoint('register', { "username": username, 'password': pasword, 'email': email, 'repeat_password': repeat_password })
    assert res.status_code ==  200
    res_body = res.json()
    assert res_body['success'] == True
    """

def test_login():
    res = return_endpoint('login', '') 
    assert res.status_code == 400
    res = return_endpoint('login', { "username": "angel" })
    assert res.status_code == 400
    res = return_endpoint('login', { "username": "not_valid_user", "password": "nojejejej" })
    assert res.status_code == 401
    res = return_endpoint('login', { "username": "angel", "password": "invalid_apassword" })
    assert res.status_code == 401

    res = return_endpoint('register', { "username": 'angel', 'password': 'angel', 'email': 'angel', 'repeat_password': 'angel' })
    res = return_endpoint('login', { "username": "angel", "password": "angel" })
    assert res.status_code == 200
    res_body = res.json()
    assert res_body['success'] == True




